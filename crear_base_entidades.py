# crear_base_entidades.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import cadena_base_datos

# Crear motor de conexión
engine = create_engine(cadena_base_datos, echo=False)

# Clase base para los modelos
Base = declarative_base()


class Clinica(Base):
    __tablename__ = "clinica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_comercial = Column(String(100), nullable=False)
    direccion = Column(String(150), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    # Relación 1 a muchos: Una clínica tiene varios consultorios
    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return (
            f"Clínica(id={self.id}, nombre='{self.nombre_comercial}', "
            f"dirección='{self.direccion}', responsable='{self.veterinario_responsable}')"
        )


class Consultorio(Base):
    __tablename__ = "consultorio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_o_numero = Column(String(50), nullable=False)
    especialidad = Column(String(80), nullable=False)

    # Asociación obligatoria a una sola clínica
    clinica_id = Column(Integer, ForeignKey("clinica.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    # Relación 1 a muchos: Un consultorio tiene uno o varios veterinarios
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return (
            f"Consultorio(id={self.id}, nombre_o_numero='{self.nombre_o_numero}', "
            f"especialidad='{self.especialidad}', clinica_id={self.clinica_id})"
        )


class Veterinario(Base):
    __tablename__ = "veterinario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(80), nullable=False)
    apellidos = Column(String(80), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    numero_licencia = Column(String(50), nullable=False, unique=True)

    # Asociación obligatoria a un único consultorio
    consultorio_id = Column(Integer, ForeignKey("consultorio.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    # Relación 1 a muchos: Un veterinario elabora varias historias clínicas
    historias_clinicas = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return (
            f"Veterinario(id={self.id}, nombre='{self.nombres} {self.apellidos}', "
            f"correo='{self.correo}', licencia='{self.numero_licencia}')"
        )


class HistoriaClinica(Base):
    __tablename__ = "historia_clinica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico_principal = Column(String(200), nullable=False)
    tratamiento_prescrito = Column(String(200), nullable=False)
    nombre_mascota = Column(String(80), nullable=False)

    # Asociación obligatoria al veterinario que la elaboró
    veterinario_id = Column(Integer, ForeignKey("veterinario.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias_clinicas")

    def __repr__(self):
        return (
            f"HistoriaClinica(id={self.id}, fecha={self.fecha_atencion}, "
            f"mascota='{self.nombre_mascota}', diagnóstico='{self.diagnostico_principal}', "
            f"tratamiento='{self.tratamiento_prescrito}')"
        )


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos y entidades creadas correctamente.")

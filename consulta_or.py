from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_base_entidades import Consultorio

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

consultorios = (
    session.query(Consultorio)
    .filter(
        or_(
            Consultorio.especialidad == "Cirugía",
            Consultorio.especialidad == "Dermatología",
        )
    )
    .all()
)

print("=== Consultorios de Cirugía o Dermatología (or_) ===")
for c in consultorios:
    print(f"{c.nombre_o_numero} | Especialidad: {c.especialidad} | Clínica: {c.clinica.nombre_comercial}")

session.close()

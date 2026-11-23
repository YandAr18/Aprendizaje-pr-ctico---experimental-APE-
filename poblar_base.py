# poblar_base.py
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Crear Clínicas
clinica1 = Clinica(
    nombre_comercial="Clínica Veterinaria Vida Animal",
    direccion="Av. Universitaria y Lourdes, Loja",
    veterinario_responsable="Dr. Carlos Mendoza",
)
clinica2 = Clinica(
    nombre_comercial="Hospital Veterinario Huellas",
    direccion="Av. 6 de Diciembre N34-120, Quito",
    veterinario_responsable="Dra. Valeria Paredes",
)
clinica3 = Clinica(
    nombre_comercial="Clínica Mascota Feliz",
    direccion="Av. Francisco de Orellana, Guayaquil",
    veterinario_responsable="Dr. Andrés Salazar",
)

session.add_all([clinica1, clinica2, clinica3])
session.flush()  # Asigna IDs sin cerrar aún la transacción

# 2. Crear Consultorios asociados a cada Clínica
cons1 = Consultorio(
    nombre_o_numero="Consultorio 101",
    especialidad="Medicina General",
    clinica=clinica1,
)
cons2 = Consultorio(
    nombre_o_numero="Consultorio 102",
    especialidad="Cirugía",
    clinica=clinica1,
)
cons3 = Consultorio(
    nombre_o_numero="Consultorio A1",
    especialidad="Dermatología",
    clinica=clinica2,
)
cons4 = Consultorio(
    nombre_o_numero="Consultorio A2",
    especialidad="Cirugía",
    clinica=clinica2,
)
cons5 = Consultorio(
    nombre_o_numero="Consultorio 1",
    especialidad="Medicina General",
    clinica=clinica3,
)

session.add_all([cons1, cons2, cons3, cons4, cons5])
session.flush()

# 3. Crear Veterinarios asociados a cada Consultorio
vet1 = Veterinario(
    nombres="Juan Pablo",
    apellidos="Ríos",
    correo="juan.rios@vidaanimal.ec",
    numero_licencia="LIC-VET-1001",
    consultorio=cons1,
)
vet2 = Veterinario(
    nombres="María Fernanda",
    apellidos="Gómez",
    correo="maria.gomez@vidaanimal.ec",
    numero_licencia="LIC-VET-1002",
    consultorio=cons2,
)
vet3 = Veterinario(
    nombres="Luis Alberto",
    apellidos="Torres",
    correo="luis.torres@huellas.ec",
    numero_licencia="LIC-VET-2001",
    consultorio=cons3,
)
vet4 = Veterinario(
    nombres="Sofía",
    apellidos="Cordero",
    correo="sofia.cordero@huellas.ec",
    numero_licencia="LIC-VET-2002",
    consultorio=cons4,
)
vet5 = Veterinario(
    nombres="Diego",
    apellidos="Armijos",
    correo="diego.armijos@mascotafeliz.ec",
    numero_licencia="LIC-VET-3001",
    consultorio=cons5,
)

session.add_all([vet1, vet2, vet3, vet4, vet5])
session.flush()

# 4. Crear Historias Clínicas asociadas a cada Veterinario
hc1 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 5),
    diagnostico_principal="Gastroenteritis leve",
    tratamiento_prescrito="Dieta blanda e hidratación oral",
    nombre_mascota="Max",
    veterinario=vet1,
)
hc2 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 12),
    diagnostico_principal="Otitis externa",
    tratamiento_prescrito="Gotas óticas antibióticas por 7 días",
    nombre_mascota="Luna",
    veterinario=vet1,
)
hc3 = HistoriaClinica(
    fecha_atencion=date(2026, 11, 2),
    diagnostico_principal="Fractura de radio",
    tratamiento_prescrito="Inmovilización y cirugía ortopédica",
    nombre_mascota="Rocky",
    veterinario=vet2,
)
hc4 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 20),
    diagnostico_principal="Dermatitis alérgica",
    tratamiento_prescrito="Antihistamínico y baño medicado",
    nombre_mascota="Nala",
    veterinario=vet3,
)
hc5 = HistoriaClinica(
    fecha_atencion=date(2026, 11, 15),
    diagnostico_principal="Esterilización programada",
    tratamiento_prescrito="Analgésicos y reposo postoperatorio",
    nombre_mascota="Kira",
    veterinario=vet4,
)
hc6 = HistoriaClinica(
    fecha_atencion=date(2026, 11, 18),
    diagnostico_principal="Otitis externa",
    tratamiento_prescrito="Limpieza auricular y antiinflamatorio",
    nombre_mascota="Toby",
    veterinario=vet5,
)

session.add_all([hc1, hc2, hc3, hc4, hc5, hc6])
session.commit()
session.close()

print("Datos ingresados correctamente en la base de datos.")

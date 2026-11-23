from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_base_entidades import Consultorio

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

consultorios_cirugia = (
    session.query(Consultorio)
    .filter(Consultorio.especialidad == "Cirugía")
    .all()
)

print("=== Consultorios de especialidad Cirugía (filter) ===")
for c in consultorios_cirugia:
    print(f"{c.nombre_o_numero} | Clínica: {c.clinica.nombre_comercial}")

session.close()

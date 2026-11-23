from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_base_entidades import Clinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todas las clínicas usando .all()
clinicas = session.query(Clinica).all()

print("=== Clínicas y número de Historias Clínicas asociadas ===")
for clinica in clinicas:
    total_historias = 0
    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias_clinicas)

    print(
        f"Clínica: {clinica.nombre_comercial} "
        f"(Responsable: {clinica.veterinario_responsable}) -> "
        f"Historias Clínicas asociadas: {total_historias}"
    )

session.close()

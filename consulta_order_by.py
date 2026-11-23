from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_base_entidades import HistoriaClinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

historias_ordenadas = (
    session.query(HistoriaClinica)
    .order_by(HistoriaClinica.fecha_atencion.desc())
    .all()
)

print("=== Historias Clínicas ordenadas por fecha (order_by) ===")
for h in historias_ordenadas:
    print(
        f"Fecha: {h.fecha_atencion} | Mascota: {h.nombre_mascota} | "
        f"Diagnóstico: {h.diagnostico_principal} | "
        f"Veterinario: {h.veterinario.nombres} {h.veterinario.apellidos}"
    )

session.close()

from datetime import date
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_base_entidades import HistoriaClinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

historias = (
    session.query(HistoriaClinica)
    .filter(
        and_(
            HistoriaClinica.diagnostico_principal == "Otitis externa",
            HistoriaClinica.fecha_atencion >= date(2026, 11, 1),
        )
    )
    .all()
)

print("=== Historias con Otitis externa desde noviembre 2026 (and_) ===")
for h in historias:
    print(f"Mascota: {h.nombre_mascota} | Fecha: {h.fecha_atencion} | Tratamiento: {h.tratamiento_prescrito}")

session.close()

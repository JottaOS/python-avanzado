from database import engine
from models import Calificacion, Estudiante, Evaluacion, Inscripcion
from sqlalchemy import select
from sqlalchemy.orm import Session

"""
SELECT e.*, es.nombre FROM evaluaciones e 
INNER JOIN inscripciones i ON e.curso_id = i.curso_id 
INNER JOIN estudiantes es ON es.id  = i.estudiante_id 
WHERE e.tipo = 'Tarea' AND e.etapa = 1 ;
"""


def parte_2():
    with Session(engine) as session:
        resultados = (
            session.execute(
                select(
                    Evaluacion.id,
                    Evaluacion.curso_id,
                    Evaluacion.etapa,
                    Evaluacion.tipo,
                    (Evaluacion.id).label("evaluacion_id"),
                )
                .join(Inscripcion, Evaluacion.curso_id == Inscripcion.curso_id)
                .join(Estudiante, Inscripcion.estudiante_id == Estudiante.id)
            )
            .scalars()
            .all()
        )

        filtrados = filter(
            lambda item: item["tipo"] == "Tarea" and item["etapa"] == 1, resultados
        )

        calificaciones = (
            session.execute(
                select(Calificacion).where(
                    Calificacion.evaluacion_id in filtrados["id"]
                    and Calificacion.inscripcion_id in filtrados["inscripcion_id"]
                )
            )
            .scalars()
            .all()
        )

        calificaciones = map(  # noqa: C417
            lambda x: {**x, "nota": x["nota"] + 10}, calificaciones
        )

        session.commit()

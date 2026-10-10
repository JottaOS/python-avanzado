import pandas as pd
from database import engine
from models import (
    Calificacion,
    Curso,
    Estudiante,
    Evaluacion,
    Inscripcion,
    Materia,
    Profesor,
)
from sqlalchemy import select
from sqlalchemy.orm import Session

"""SELECT * FROM calificaciones c 
JOIN inscripciones i ON c.inscripcion_id = i.id 
JOIN evaluaciones e ON c.evaluacion_id = e.id 
JOIN estudiantes es ON i.estudiante_id = es.id 
JOIN cursos cur ON i.curso_id = cur.id 
JOIN profesores p ON cur.profesor_id  = p.id 
JOIN materias m ON cur.materia_id = m.id 
"""

PESOS_POR_ETAPA = {1: 0.3, 2: 0.3, 3: 0.4}


def parte_3():
    with Session(engine) as session:
        stmt = (
            select(
                Calificacion,
                Inscripcion,
                Evaluacion,
                Estudiante,
                Curso,
                Profesor.Profesor,
                Materia,
            )
            .join(Inscripcion, Calificacion.inscripcion_id == Inscripcion.id)
            .join(Evaluacion, Calificacion.evaluacion_id == Evaluacion.id)
            .join(Estudiante, Inscripcion.estudiante_id == Estudiante.id)
            .join(Curso, Inscripcion.curso_id == Curso.id)
            .join(Profesor, Curso.profesor_id == Profesor.id)
            .join(Materia, Curso.materia_id == Materia.id)
        )

        resultados = session.execute(stmt).all()

        df = pd.DataFrame(resultados)
        # for item in df.items():
        #     print(item)

        nota_final = (
            df["nota"] * (df["porcentaje_etapa"] / 100) * PESOS_POR_ETAPA[df["etapa"]]
        )
        print(nota_final)

        agrupado_profesores = df.groupby(Profesor)
        print(agrupado_profesores)

        return agrupado_profesores

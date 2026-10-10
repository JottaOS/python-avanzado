from database import Base
from sqlalchemy import CheckConstraint, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


class Profesor(Base):
    # Profesor: id (PK, int), nombre (varchar 100), email (varchar 100).
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))


class Estudiante(Base):
    #  Estudiante: id (PK, int), nombre (varchar 100), matricula (varchar 20, unique).
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    matricula: Mapped[str] = mapped_column(String(20), unique=True)


class Materia(Base):
    #  Materia: id (PK, int), nombre (varchar 100), codigo (varchar 20, unique).
    __tablename__ = "materias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    codigo: Mapped[str] = mapped_column(String(20), unique=True)


class Curso(Base):
    # Curso: id (PK, int), materia_id (FK a materias.id),
    # profesor_id (FK a profesores.id), anio (int), seccion (varchar 5).
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    materia_id: Mapped[int] = mapped_column(ForeignKey("materias.id"))
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    anio: Mapped[int] = mapped_column()
    seccion: Mapped[str] = mapped_column(String(5))


class Inscripcion(Base):
    # Inscripcion: id (PK, int), estudiante_id (FK a estudiantes.id), curso_id (FK a cursos.id).
    __tablename__ = "inscripciones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"))
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))


class Evaluacion(Base):
    # Evaluacion: id (PK, int), curso_id (FK a cursos.id), etapa (int)
    # tipo (varchar 20: 'Tarea', 'Parcial', 'Final'), porcentaje_etapa (float entre 0 y 100).
    __tablename__ = "evaluaciones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    etapa: Mapped[int] = mapped_column()
    tipo: Mapped[str] = mapped_column(
        String(
            20,
            CheckConstraint(
                "tipo IN ('Tarea', 'Parcial', 'Final')",
                name="check_tipo_evaluacion",
            ),
        ),
    )
    porcentaje_etapa: Mapped[Float] = mapped_column(
        Float(
            12,
            CheckConstraint(
                "porcentaje_etapa >= 0 AND porcentaje_etapa <= 100",
                name="check_porcentaje_etapa_evaluacion",
            ),
        ),
    )


class Calificacion(Base):
    # Calificacion: id (PK, int), inscripcion_id (FK a inscripciones.id),
    # evaluacion_id (FK a evaluaciones.id), nota (float de 0 a 100)

    __tablename__ = "calificaciones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    inscripcion_id: Mapped[int] = mapped_column(ForeignKey("inscripciones.id"))
    evaluacion_id: Mapped[int] = mapped_column(ForeignKey("evaluaciones.id"))
    nota: Mapped[Float] = mapped_column(
        Float(
            12,
            CheckConstraint(
                "nota >= 0 AND nota <= 100",
                name="check_nota_calificacion",
            ),
        )
    )

-- Desactivar temporalmente la revisión de claves foráneas para la limpieza

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE calificaciones;

TRUNCATE TABLE evaluaciones;

TRUNCATE TABLE inscripciones;

TRUNCATE TABLE estudiantes;

TRUNCATE TABLE cursos;

TRUNCATE TABLE materias;

TRUNCATE TABLE profesores;

SET FOREIGN_KEY_CHECKS = 1;



-- ==============================================================================

-- 1. INSERTAR PROFESORES

-- ==============================================================================

INSERT INTO profesores (id, nombre, email) VALUES

(1, 'Dr. Carlos Mendoza', 'cmendoza@escuela.edu'),

(2, 'Dra. Ana Martínez', 'amartinez@escuela.edu'),

(3, 'Ing. Roberto Gómez', 'rgomez@escuela.edu');



-- ==============================================================================

-- 2. INSERTAR MATERIAS

-- ==============================================================================

INSERT INTO materias (id, nombre, codigo) VALUES

(1, 'Programación Python', 'PY101'),

(2, 'Bases de Datos', 'BD201');



-- ==============================================================================

-- 3. INSERTAR CURSOS (Misma materia puede tener múltiples cursos y profesores)

-- ==============================================================================

INSERT INTO cursos (id, materia_id, profesor_id, anio, seccion) VALUES

(1, 1, 1, 2026, 'A'), -- Python Sección A - Dr. Carlos Mendoza

(2, 1, 2, 2026, 'B'), -- Python Sección B - Dra. Ana Martínez

(3, 2, 3, 2026, 'A'); -- Base de Datos Sección A - Ing. Roberto Gómez



-- ==============================================================================

-- 4. INSERTAR ESTUDIANTES

-- ==============================================================================

INSERT INTO estudiantes (id, nombre, matricula) VALUES

(1, 'Juan Pérez', 'EST-001'),

(2, 'María Gómez', 'EST-002'),

(3, 'Luis Torres', 'EST-003'),

(4, 'Sofia Benítez', 'EST-004'),

(5, 'Diego Alonso', 'EST-005'),

(6, 'Laura Rojas', 'EST-006');



-- ==============================================================================

-- 5. INSERTAR INSCRIPCIONES

-- ==============================================================================

INSERT INTO inscripciones (id, estudiante_id, curso_id) VALUES

(1, 1, 1), -- Juan Pérez en Python A

(2, 2, 1), -- María Gómez en Python A

(3, 3, 2), -- Luis Torres en Python B

(4, 4, 2), -- Sofia Benítez en Python B

(5, 5, 3), -- Diego Alonso en Base de Datos A

(6, 6, 3); -- Laura Rojas en Base de Datos A



-- ==============================================================================

-- 6. INSERTAR EVALUACIONES

-- Regla de Pesos por Etapa: Etapa 1 (30%), Etapa 2 (30%), Etapa 3 (40%)

-- ==============================================================================



-- Evaluaciones Curso 1 (Python A): 2 Tareas + 1 Parcial en Etapa 1

INSERT INTO evaluaciones (id, curso_id, etapa, tipo, porcentaje_etapa) VALUES

(1, 1, 1, 'Tarea', 15.0),    -- Tarea 1 de Etapa 1 (15% de la Etapa 1)

(2, 1, 1, 'Tarea', 15.0),    -- Tarea 2 de Etapa 1 (15% de la Etapa 1)

(3, 1, 1, 'Parcial', 70.0),  -- Parcial de Etapa 1 (70% de la Etapa 1)

(4, 1, 2, 'Parcial', 100.0), -- Parcial de Etapa 2 (100% de la Etapa 2)

(5, 1, 3, 'Final', 100.0);   -- Examen Final (100% de la Etapa 3)



-- Evaluaciones Curso 2 (Python B): 1 Tarea + 1 Parcial en Etapa 1

INSERT INTO evaluaciones (id, curso_id, etapa, tipo, porcentaje_etapa) VALUES

(6, 2, 1, 'Tarea', 30.0),

(7, 2, 1, 'Parcial', 70.0),

(8, 2, 2, 'Parcial', 100.0),

(9, 2, 3, 'Final', 100.0);



-- Evaluaciones Curso 3 (Base de Datos A): 1 Tarea + 1 Parcial en Etapa 1

INSERT INTO evaluaciones (id, curso_id, etapa, tipo, porcentaje_etapa) VALUES

(10, 3, 1, 'Tarea', 20.0),

(11, 3, 1, 'Parcial', 80.0),

(12, 3, 2, 'Parcial', 100.0),

(13, 3, 3, 'Final', 100.0);



-- ==============================================================================

-- 7. INSERTAR CALIFICACIONES DE PRUEBA

-- ==============================================================================



-- --- CURSO 1 (Dr. Carlos Mendoza) ---

-- Juan Pérez (Inscripción 1): Entregó TODAS las Tareas de Etapa 1 -> ¡RECIBE BONIFICACIÓN (+10 pts)!

INSERT INTO calificaciones (inscripcion_id, evaluacion_id, nota) VALUES

(1, 1, 85.0), -- Tarea 1 Etapa 1

(1, 2, 90.0), -- Tarea 2 Etapa 1

(1, 3, 65.0), -- Parcial Etapa 1

(1, 4, 75.0), -- Parcial Etapa 2

(1, 5, 80.0); -- Final Etapa 3



-- María Gómez (Inscripción 2): NO entregó la Tarea 2 de Etapa 1 -> NO RECIBE BONIFICACIÓN

INSERT INTO calificaciones (inscripcion_id, evaluacion_id, nota) VALUES

(2, 1, 70.0), -- Tarea 1 Etapa 1

              -- (Falta Tarea 2)

(2, 3, 50.0), -- Parcial Etapa 1

(2, 4, 55.0), -- Parcial Etapa 2

(2, 5, 60.0); -- Final Etapa 3



-- --- CURSO 2 (Dra. Ana Martínez) ---

-- Luis Torres (Inscripción 3): Entregó TODAS las Tareas de Etapa 1 -> ¡RECIBE BONIFICACIÓN (+10 pts)!

INSERT INTO calificaciones (inscripcion_id, evaluacion_id, nota) VALUES

(3, 6, 95.0), -- Tarea Etapa 1

(3, 7, 88.0), -- Parcial Etapa 1

(3, 8, 90.0), -- Parcial Etapa 2

(3, 9, 92.0); -- Final Etapa 3



-- Sofia Benítez (Inscripción 4): NO entregó la Tarea de Etapa 1 -> NO RECIBE BONIFICACIÓN

INSERT INTO calificaciones (inscripcion_id, evaluacion_id, nota) VALUES

              -- (Falta Tarea Etapa 1)

(4, 7, 60.0), -- Parcial Etapa 1

(4, 8, 65.0), -- Parcial Etapa 2

(4, 9, 58.0); -- Final Etapa 3



-- --- CURSO 3 (Ing. Roberto Gómez) ---

-- Diego Alonso (Inscripción 5): Entregó TODAS las Tareas de Etapa 1 -> ¡RECIBE BONIFICACIÓN (+10 pts)!

INSERT INTO calificaciones (inscripcion_id, evaluacion_id, nota) VALUES

(5, 10, 60.0), -- Tarea Etapa 1

(5, 11, 45.0), -- Parcial Etapa 1

(5, 12, 50.0), -- Parcial Etapa 2

(5, 13, 55.0); -- Final Etapa 3



-- Laura Rojas (Inscripción 6): Entregó TODAS las Tareas de Etapa 1 -> ¡RECIBE BONIFICACIÓN (+10 pts)!

INSERT INTO calificaciones (inscripcion_id, evaluacion_id, nota) VALUES

(6, 10, 100.0), -- Tarea Etapa 1 (Con bonificación no debe pasar de 100.0)

(6, 11, 95.0),  -- Parcial Etapa 1

(6, 12, 92.0),  -- Parcial Etapa 2

(6, 13, 98.0);  -- Final Etapa 3
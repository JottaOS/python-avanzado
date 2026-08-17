class Persona:
    def __init__(self, nombre, edad, ci, telefono):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci
        self.telefono = telefono

    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años, mi cédula es {self.ci} y mi teléfono es {self.telefono}."

    def __str__(self):
        return self.presentarse()


class Medico(Persona):
    def __init__(self, nombre, edad, ci, especialidad, telefono):
        super().__init__(nombre, edad, ci, telefono)
        self.especialidad = especialidad

    def presentarse(self):
        base = super().presentarse()
        return f"{base} Soy médico especialista en {self.especialidad}."

    def atender(self, paciente):
        return f"Dr. {self.nombre} está atendiendo a {paciente.nombre}."


class Enfermero(Persona):
    def __init__(self, nombre, edad, ci, turno, telefono):
        super().__init__(nombre, edad, ci, telefono)
        self.turno = turno

    def presentarse(self):
        base = super().presentarse()
        return f"{base} Trabajo como enfermero turno {self.turno}."

    def registrar_signos_vitales(self, paciente):
        return f"{self.nombre} registró los signos vitales de {paciente.nombre}."


class Paciente(Persona):
    def __init__(self, nombre, edad, ci, diagnostico, telefono):
        super().__init__(nombre, edad, ci, telefono)
        self.diagnostico = diagnostico

    def presentarse(self):
        base = super().presentarse()
        return f"{base} Estoy internado por: {self.diagnostico}."

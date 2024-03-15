class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Comprador(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

class Organizador(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
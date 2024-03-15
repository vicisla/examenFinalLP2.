from abc import ABC, abstractmethod

class Evento(ABC):
    @abstractmethod
    def mostrar_detalle(self):
        pass

class EventoParrillada(Evento):
    def __init__(self, fecha, lugar, precio):
        self.fecha = fecha
        self.lugar = lugar
        self.precio = precio

    def mostrar_detalle(self):
        return f"Parrillada el {self.fecha} en {self.lugar}. Precio: ${self.precio}"

class EventoVIP(EventoParrillada):
    def __init__(self, fecha, lugar, precio, beneficios):
        super().__init__(fecha, lugar, precio)
        self.beneficios = beneficios

    def mostrar_detalle(self):
        return f"Parrillada VIP el {self.fecha} en {self.lugar}. Precio: ${self.precio}. Beneficios: {self.beneficios}"
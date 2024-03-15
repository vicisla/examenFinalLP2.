import json

from eventos import EventoParrillada, EventoVIP
from personas import Comprador

class Venta:
    def __init__(self, comprador, evento, cantidad):
        self.comprador = comprador
        self.evento = evento
        self.cantidad = cantidad

class GestorVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def reporte_ventas_evento(self, evento):
        total_ventas = sum(venta.cantidad for venta in self.ventas if venta.evento == evento)
        return f"Total de ventas para el evento {evento.mostrar_detalle()}: {total_ventas}"

    def reporte_ventas_totales(self):
        total_ventas = sum(venta.cantidad for venta in self.ventas)
        return f"Total de ventas en todos los eventos: {total_ventas}"

    def guardar_ventas_json(self, filename):
        ventas_json = [{'comprador': venta.comprador.nombre, 'evento': vars(venta.evento), 'cantidad': venta.cantidad} for venta in self.ventas]
        with open(filename, 'w') as file:
            json.dump(ventas_json, file)

    def cargar_ventas_json(self, filename):
        try:
            with open(filename, 'r') as file:
                ventas_json = json.load(file)
                for venta_data in ventas_json:
                    comprador = Comprador(venta_data['comprador'], "")
                    evento_data = venta_data['evento']
                    if 'beneficios' in evento_data:  # Determina si es un EventoVIP
                        evento = EventoVIP(**evento_data)
                    else:
                        evento = EventoParrillada(**evento_data)
                    venta = Venta(comprador, evento, venta_data['cantidad'])
                    self.ventas.append(venta)
        except FileNotFoundError:
            raise FileNotFoundError("El archivo de ventas no se encontró.")
        except Exception as e:
            raise Exception("Error al cargar ventas desde el archivo JSON:", e)
        
class EventoAgotadoException(Exception):
    pass

class DatosInvalidosException(Exception):
    pass

class ProblemaArchivoException(Exception):
    pass
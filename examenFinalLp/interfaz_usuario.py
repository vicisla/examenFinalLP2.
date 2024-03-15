from personas import Comprador
from eventos import EventoParrillada, EventoVIP
from ventas import Venta, GestorVentas

def realizar_venta(gestor_ventas):
    print("Realizar una venta:")
    nombre_comprador = input("Ingrese el nombre del comprador: ")
    email_comprador = input("Ingrese el email del comprador: ")
    comprador = Comprador(nombre_comprador, email_comprador)
    
    print("Seleccione el tipo de evento:")
    print("1. Parrillada Regular")
    print("2. Parrillada VIP")
    opcion_evento = input("Ingrese el número correspondiente al tipo de evento: ")

    fecha = input("Ingrese la fecha del evento: ")
    lugar = input("Ingrese el lugar del evento: ")
    precio = float(input("Ingrese el precio del evento: "))

    if opcion_evento == "1":
        evento = EventoParrillada(fecha, lugar, precio)
    elif opcion_evento == "2":
        beneficios = input("Ingrese los beneficios del evento VIP: ")
        evento = EventoVIP(fecha, lugar, precio, beneficios)
    else:
        print("Opción inválida.")
        return
    
    cantidad = int(input("Ingrese la cantidad de entradas a vender: "))
    venta = Venta(comprador, evento, cantidad)
    gestor_ventas.agregar_venta(venta)
    print("Venta realizada con éxito.")

def reportes_ventas(gestor_ventas):
    print("Reportes de ventas:")
    print("1. Reporte de ventas por evento")
    print("2. Reporte de ventas totales")
    opcion_reporte = input("Seleccione una opción de reporte: ")

    if opcion_reporte == "1":
        print("Seleccione el evento:")
        for index, venta in enumerate(gestor_ventas.ventas, start=1):
            print(f"{index}. {venta.evento.mostrar_detalle()}")
        opcion_evento = int(input("Ingrese el número correspondiente al evento: "))
        evento_seleccionado = gestor_ventas.ventas[opcion_evento - 1].evento
        print(gestor_ventas.reporte_ventas_evento(evento_seleccionado))
    elif opcion_reporte == "2":
        print(gestor_ventas.reporte_ventas_totales())
    else:
        print("Opción inválida.")
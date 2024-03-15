from interfaz_usuario import realizar_venta, reportes_ventas
from ventas import GestorVentas

def menu_principal():
    print("Bienvenido al sistema de gestión de ventas de tickets para eventos de parrilladas.")
    print("1. Comprar tickes")
    print("2. Mostrar ventas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    gestor_ventas = GestorVentas()
    while True:
        opcion = menu_principal()
        if opcion == "1":
            realizar_venta(gestor_ventas)
        elif opcion == "2":
            reportes_ventas(gestor_ventas)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
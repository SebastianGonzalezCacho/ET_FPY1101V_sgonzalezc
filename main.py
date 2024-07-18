import Funciones as F

def mostrar_menu():
    print("Menú de los empleados")
    print("1. Asigna sueldos aleatorios")
    print("2. Ver estadisticas")
    print("3. Reporte sueldos")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            F.asignar_sueldos_aleatorios()
        elif opcion == '2':
            F.ver_estadistica()
            F.lista_sueldo()
        elif opcion == '3':
            F.reporte_sueldos()
        elif opcion == '4':
            print("Finalizando el programa...")
            print("Desarrollado por Sebastián González Cacho")
            print("Rut 16.210.808-5")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

import servicios

print("Programa principal de los servicios")


def principal():
    n = servicios.validar(0, "Ingrese la cantidad de servicios: ")
    servicio = [None] * n

    opcion = 0
    print("Menú de opciones")
    print("1. Carga del arreglo")
    print("2. Muestra del arreglo ordenado")
    print("3. Cantidad de servicios por tipo")
    print("4. Búesqueda de datos (descripción y personal afectado)")
    print("5. Programa finalizado")

    while opcion != 5:
        opcion = int(input("Elija una opcion: "))

        if opcion == 1:
            servicios.opcion1(servicio)
        elif opcion == 2:
            servicios.opcion2(servicio)
        elif opcion == 3:
            servicios.opcion3(servicio)
        elif opcion == 4:
            servicios.opcion4(servicio)
        else:
            print("Programa finalizado")


if __name__ == "__main__":
    principal()
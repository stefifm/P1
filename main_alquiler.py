import alquiler

print("Programa principal")


def principal():
    n = alquiler.validar(0,"Ingrese el tamaño del arreglo: ")
    alq = [None] * n

    opcion = 0
    print("Menú de opciones")
    print("1- Cargue el arreglo")
    print("2- Muestra del listado de alquileres ordenado por tipo")
    print("3- Cantidad de alquileres por tipo de coche")
    print("4- Búsqueda")
    print("5- Salir")

    while opcion != 5:
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            alquiler.opcion1(alq)
        elif opcion == 2:
            alquiler.opcion2(alq)
        elif opcion == 3:
            alquiler.opcion3(alq)
        elif opcion == 4:
            alquiler.opcion4(alq)
        else:
            print("Programa finalizado")


if __name__ == "__main__":
    principal()
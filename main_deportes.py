import deportes

print("Programa principal")


def principal():
    n = deportes.validar(0,"Ingrese el tamaño del arreglo: ")
    alquiler_sport = [None] * n

    opcion = 0
    print("Menú de opciones")
    print("1- Cargue el arreglo ")
    print("2- Listado de artículos ordenados ")
    print("3- Costos y promedio ")
    print("4- Búsqueda de la descricpión ")
    print("5- Costo acumulado ")
    print("6- Programa finalizado")
    while opcion != 6:
        opcion = int(input("Elija su opción: "))

        if opcion == 1:
            deportes.opcion1(alquiler_sport)
        elif opcion == 2:
            deportes.opcion2(alquiler_sport)
        elif opcion == 3:
            deportes.opcion3(alquiler_sport)
        elif opcion == 4:
            deportes.opcion4(alquiler_sport)
        elif opcion == 5:
            deportes.opcion5(alquiler_sport)
        else:
            print("Programa finalizado")


if __name__ == '__main__':
    principal()
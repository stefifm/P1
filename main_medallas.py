import medallas
print("Programa principal del medallero olímpico")



def principal():
    n = medallas.validar(0, "Ingrese la cantidad de países: ")
    pais = [None] * n
    medallas.carga_automatica(pais)

    opcion = 0
    print("Menú de opciones")
    print("1. Muestra ordenada de la lista de países")
    print("2. Promedio de medallas de oro")
    print("3. País con la mayor cantidad de medallas de plata")
    print("4. Países solo medalla de bronce")
    print("5. Países por continente")
    print("6. Programa finalizado")

    while opcion != 6:
        opcion = int(input("Ingrese la opción seleccionada: "))

        if opcion == 1:
            medallas.opcion1(pais)
        elif opcion == 2:
            medallas.opcion2(pais)
        elif opcion == 3:
            medallas.opcion3(pais)
        elif opcion == 4:
            medallas.opcion4(pais)
        elif opcion == 5:
            medallas.opcion5(pais)
        else:
            print("----------Programa Finalizado----------")


if __name__ == "__main__":
    principal()
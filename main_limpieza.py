import limpieza

print("Programa princiapl del alquiler de servicios de limpieza")



def principal():
    n = limpieza.validar(0, "Ingrese la cantidad de trabajos ofrecidos: ")
    serv_limpieza = [None] * n

    opcion = 0
    print("Menú de opciones")
    print("1. Carga del arreglo de forma automática")
    print("2. Muestra de la lista ordenada de mayor a menor")
    print("3. Mayor cantidad de personal")
    print("4. Búsqueda de la descripción o nombre del trabajo")
    print("5. Trabajos por tipo")
    print("6. Programa finalizado")

    while opcion != 6:
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            limpieza.opcion1(serv_limpieza)
        elif opcion == 2:
            limpieza.opcion2(serv_limpieza)
        elif opcion == 3:
            limpieza.opcion3(serv_limpieza)
        elif opcion == 4:
            limpieza.opcion4(serv_limpieza)
        elif opcion == 5:
            limpieza.opcion5(serv_limpieza)
        else:
            print("Programa finalizado")

if __name__ == "__main__":
    principal()
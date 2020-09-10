import barcos

print("Programa principal del puerto de la ciudad")

def principal():
    n = barcos.validar(0, "Ingrese la cantidad de barcos: ")
    barco = [None] * n

    opcion = 0
    print("Menù de opciones")
    print("1. Cargar el arreglo")
    print("2. Muestra ordenada de mayor a menor de la lista de barcos")
    print("3. Cantidad total de barcos por tipo")
    print("4. Barco con menor cantidad de días en el puerto")
    print("5. Búsqueda de la empresa propietaria")
    print("6. Programa finalizado")

    while opcion != 6:
        opcion = int(input("Ingrese la opción elegida: "))

        if opcion == 1:
            barcos.opcion1(barco)
        elif opcion == 2:
            barcos.opcion2(barco)
        elif opcion == 3:
            barcos.opcion3(barco)
        elif opcion == 4:
            barcos.opcion4(barco)
        elif opcion == 5:
            barcos.opcion5(barco)
        else:
            print("Programa finalizado")


if __name__ == "__main__":
    principal()
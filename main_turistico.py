import turistico

print("Programa principal de agencia de servicio turístico")


def principal():
    n = turistico.validar(0, "Ingrese la cantidad de paquetes: ")
    serv_turistico = [None] * n
    opcion = 0
    print("Menú de opciones")
    print("1. Carga del arreglo")
    print("2. Listado de paquetes")
    print("3. Cantidad de paquetes por tipo")
    print("4. Búsqueda de número de identifación e importe del paquete")
    print("5. Programa finalizado")

    while opcion != 5:
        opcion = int(input("Ingrese la opción elegida: "))

        if opcion == 1:
            turistico.opcion1(serv_turistico)
        elif opcion == 2:
            turistico.opcion2(serv_turistico)
        elif opcion == 3:
            turistico.opcion3(serv_turistico)
        elif opcion == 4:
            turistico.opcion4(serv_turistico)
        else:
            print("Programa finalizado")

if __name__ == "__main__":
    principal()
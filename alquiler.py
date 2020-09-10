import random

print("Funciones para el ejercicio de Alquiler")

class Alquiler:
    def __init__(self, ide, desc, tipo, impor, dias):
        self.identificador = ide
        self.descripcion = desc
        self.tipo = tipo
        self.importe = impor
        self.dias = dias


def to_string(alquiler):
    r = " "
    r += "Número de la operación: " + str(alquiler.identificador)
    r += "Descripción del coche alquilado: " + alquiler.descripcion
    r += "Tipo de coche: " + str(alquiler.tipo)
    r += "Importe del aquiler: " + str(alquiler.importe)
    r += "Cantidad de días del alquiler: " + str(alquiler.dias)
    return r

#Funciones + opcion1


def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. No debe ser menor o igual a cero")
    return n

def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Valor no válido. Ingrese un valor entre",str(inf),"y",
                  str(sup))
    return n

def carga_manual(alquiler):
    for i in range(len(alquiler)):
        identificador = validar(0,"Ingrese el número de la operación: ")
        descripcion = input("Ingrese la descripción del coche: ")
        tipo = validar_rango(0, 9, "Ingrese el tipo del coche [0 al 9]: ")
        importe = float(input("Ingrese el importe del alquiler: "))
        dias = int(input("Ingrese la cantidad de días del alquiler: "))
        reg = Alquiler(identificador, descripcion, tipo, importe,dias)
        alquiler[i] = reg
    return alquiler

def opcion1(alquiler):
    print("Cargue los datos del alquiler de coches")
    carga_manual(alquiler)

#opcion 2

def orden_sort(alquiler):
    # algoritmo de selección directa
    n = len(alquiler)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if alquiler[i].importe > alquiler[j].importe:
                alquiler[i], alquiler[j] = alquiler[j], \
                                     alquiler[i]
def display(alquiler):
    for i in range(len(alquiler)):
        print(to_string(alquiler[i]))



def opcion2(alquiler):
    if alquiler[0] == None:
        print("El arreglo no está cargado")
        return
    orden_sort(alquiler)
    display(alquiler)


#opcion 3
def contador(alquiler):
    contador_tipo = [0] * 10
    for i in range(len(alquiler)):
        t = int(alquiler[i].tipo)
        contador_tipo[t] += 1
    for i in range(10):
        if contador_tipo != 0:
            print("Tipo de coche:",i,"Cantidad:",contador_tipo)

def opcion3(alquiler):
    if alquiler[0] == None:
        print("El arreglo no está cargado")
        return
    contador(alquiler)

#opcion4
def busca(alquiler, desc, dias):
    for i in range(len(alquiler)):
        if alquiler[i].descripcion == desc and alquiler[i] == dias:
            return alquiler[i]
    return None

def opcion4(alquiler):
    if alquiler[0] == None:
        print("El arreglo no está cargado")
        return
    desc = input("Ingrese la descripción a buscar: ")
    dias = int(input("Ingrese la cantidad de días a buscar: "))
    alq = busca(alquiler, desc, dias)
    if alq != None:
        print("Datos encontrados")
        print(to_string(alq))
import random

print("Funciones para el programa principal de servicios")

class Servicio:
    def __init__(self, num, desc, tipo, imp, per):
        self.numero = num
        self.descripcion = desc
        self.tipo = tipo
        self.importe = imp
        self.personal = per

def to_string(servicio):
    r = " "
    r += "Número identificatorio: " + str(servicio.numero)
    r += " - Descripción: " + str(servicio.descripcion)
    r += " - Tipo: " + str(servicio.tipo)
    r += " - Importe $: " + str(servicio.importe)
    r += " - Personal afectado: " + str(servicio.personal)
    return r

#opcion 1: carga automática

def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. No debe ser menor o igual a", inf)
    return n

def carga_automatica(servicio):
    for i in range(len(servicio)):
        numero = random.randint(100, 1000)
        descripcion = random.randint(100, 700)
        tipo = random.randint(0, 14)
        importe = random.randint(100, 1000)
        personal = random.randint(10, 1000)
        reg1 = Servicio(numero, descripcion, tipo, importe, personal)
        servicio[i] = reg1
    return servicio

def opcion1(servicio):
    print("Momento de generar el arreglo. Presione <Enter> para continuar")
    input()
    carga_automatica(servicio)
    print("Hecho. El arreglo fue generado")

#opcion2
def orden_sort(servicio):
    n = len(servicio)
    for i in range(n-1):
        for j in range(i+1, n):
            if servicio[i].numero < servicio[j].numero:
                servicio[i], servicio[j] = servicio[j], servicio[i]

def display(servicio):
    for i in range(len(servicio)):
        print(to_string(servicio[i]))

def opcion2(servicio):
    if servicio[0] == None:
        print("El arreglo no se ha generado")
        return
    orden_sort(servicio)
    display(servicio)

#opcion3

#vector de conteo

def contador(servicio):
    contador = [0] * 15
    for i in range(len(servicio)):
        k = int(servicio[i].tipo)
        contador[k] += 1
    for i in range(15):
        if contador != 0:
            print("Servicio:",i,"Cantidad de tipo de servicio ofrecido:",
                  contador[i])

def opcion3(servicio):
    if servicio[0] == None:
        print("El arreglo no se ha generado")
        return
    contador(servicio)

#opcion4
def buscar(desc, per, servicio):
    for i in range(len(servicio)):
        if servicio[i].descripcion == desc and servicio[i].personal == per:
            return servicio[i]
    return None

def opcion4(servicio):
    if servicio[0] == None:
        print("El arreglo no se ha generado")
        return
    desc = int(input("Ingrese el número de descripción a buscar: "))
    per = int(input("Ingrese la cantidad de personas a buscar: "))
    service = buscar(desc, per, servicio)
    if service != None:
        print("Datos encontrados")
        print(to_string(service))
    else:
        print("Datos no encontrados")

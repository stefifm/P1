import random

print("Servicios para el programa de servicios turísticos")

class Turistico:
    def __init__(self, num, desc, tipo, dia, imp):
        self.numero = num
        self.descripcion = desc
        self.tipo = tipo
        self.dia = dia
        self.importe = imp

def to_string(turistico):
    r = " "
    r += "Número: " + str(turistico.numero)
    r += "- Descripcion: " + turistico.descripcion
    r += "- Tipo: " + str(turistico.tipo)
    r += "- Cantidad de días: " + str(turistico.dia)
    r += "- Importe: " + str(turistico.importe)
    return r

#------------------------------------------------------------------------------

def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. No debe ser menor o igual a", inf)
    return n

def carga_automatica(turistico):
    desc = ("Paquete1", "Pauqete2", "Paquete3", "Paquete4")
    for i in range(len(turistico)):
        numero = random.randint(1, 60)
        descripcion = random.choice(desc)
        tipo = random.randint(0, 19)
        dia = random.randint(1, 30)
        importe = random.randint(100, 1000)
        t = Turistico(numero, descripcion, tipo, dia, importe)
        turistico[i] = t
    return turistico

def opcion1(turistico):
    print("Es hora de cargar el arreglo. Presione <Enter> para continuar")
    input()
    carga_automatica(turistico)
    print("Hecho. El arreglo está cargado")

#opcion2
#Ordenar de menor a mayor
def orden_sort(turistico):
    n = len(turistico)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if turistico[i].dia > turistico[j].dia:
                turistico[i], turistico[j] = turistico[j], turistico[i]

def display(turistico):
    for i in range(len(turistico)):
        print(to_string(turistico[i]))

def opcion2(turistico):
    if turistico[0] == None:
        print("El arreglo no está cargado")
        return
    orden_sort(turistico)
    display(turistico)

#opcion3
def contador(turistico):
    cont_tipo = [0] * 20
    for i in range(len(turistico)):
        t = int(turistico[i].tipo)
        cont_tipo[t] += 1
    for i in range(20):
        if cont_tipo != 0:
            print("Tipo de paquete:",i,"Cantidad de paquetes:",cont_tipo[i])

def opcion3(turistico):
    if turistico[0] == None:
        print("El arreglo no está cargado")
        return
    contador(turistico)

#Opcion4
def buscar(num, imp, turistico):
    for i in range(len(turistico)):
        if turistico[i].numero == num and turistico[i].importe == imp:
            return turistico[i]
    return None

def opcion4(turistico):
    if turistico[0] == None:
        print("El arreglo no está cargado")
        return
    num = validar(0, "Ingrese el número de identificación a buscar: ")
    imp = int(input("Ingrese el importe a buscar: "))
    tur = buscar(num, imp, turistico)
    if tur != None:
        print("Valores encontrados")
        print(to_string(tur))
    else:
        print("No se han encontrado los datos")
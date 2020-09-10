import random

print("Funciones para el alquiler de servicios de limpieza")

#clase

class Limpieza:
    def __init__(self,num, nom, tipo, imp, per):
        self.numero = num
        self.descripcion = nom
        self.tipo = tipo
        self.importe = imp
        self.personal = per

def to_string(limpieza):
    r = " "
    r += "- Número: " + str(limpieza.numero)
    r += "- Descripcion: " + limpieza.descripcion
    r += "- Tipo: " + str(limpieza.tipo)
    r += "- Importe $: " + str(limpieza.importe)
    r += "- Cantidad de personal: " + str(limpieza.personal)
    return r
#------------------------------------------------------------------------------

#opcion 1
#carga del arreglo. Uso de la opción carga automática

def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. El valor debe ser mayor a cero")
    return n

def carga_automatica(limpieza):
    nom = ("Limpieza1", "Limpieza2", "Limpieza3", "Limpieza4", "Limpieza5",
           "Limpieza6")
    for i in range(len(limpieza)):
        numero = random.randint(1, 80)
        descripcion = random.choice(nom)
        tipo = random.randint(0, 3)
        importe = round(random.random() * 100, 2)
        personal = random.randint(10, 600)
        l = Limpieza(numero, descripcion, tipo ,importe, personal)
        limpieza[i] = l
    return limpieza

def opcion1(limpieza):
    print("Hora de cargar el arreglo. Presione <Enter> para continuar")
    input()
    carga_automatica(limpieza)
    print("Hecho la carga fue realizada...")

#opcion2
def orden_sort(limpieza):
    n = len(limpieza)
    for i in range(n - 1):
        for j in range(i+1, n):
            if limpieza[i].importe < limpieza[j].importe:
                limpieza[i], limpieza[j] = limpieza[j], limpieza[i]

def display(limpieza):
    for i in range(len(limpieza)):
        print(to_string(limpieza[i]))

def opcion2(limpieza):
    if limpieza[0] == None:
        print("El arreglo no se ha cargado")
        return
    orden_sort(limpieza)
    display(limpieza)

#Opcion3
def mayor_personal(limpieza):
    mayor = limpieza[0]
    cant = len(limpieza)
    for i in range(cant):
        if limpieza[i].personal > mayor.personal:
            mayor = limpieza[i]
    return mayor

def opcion3(limpieza):
    if limpieza[0] == None:
        print("El arreglo no se ha cargado")
        return
    mayor = mayor_personal(limpieza)
    print("El trabajo",mayor.descripcion,"es el de mayor cantidad de "
                                         "personal afectado y tiene:",
          mayor.personal)

#opcion4
def buscar(desc, limpieza):
    for i in range(len(limpieza)):
        if limpieza[i].descripcion == desc:
            return limpieza[i]
    return None

def opcion4(limpieza):
    if limpieza[0] == None:
        print("El arreglo no se ha cargado")
        return
    desc = input("Ingrese el nombre del servicio de limpieza a buscar: ")
    serv = buscar(desc, limpieza)
    if serv != None:
        print("Datos encontrados")
        print(to_string(serv))
    else:
        print("No se encontraron los datos")

#opcion5
def contador(limpieza):
    cont_tipo = [0] * 4
    for i in range(len(limpieza)):
        k = int(limpieza[i].tipo)
        cont_tipo[k] += 1
    for i in range(4):
        if cont_tipo != 0:
            print("Tipo:",i,"Cantidad de trabajo por ese tipo:",cont_tipo[i])

def opcion5(limpieza):
    if limpieza[0] == None:
        print("El arreglo no se ha cargado")
        return
    contador(limpieza)
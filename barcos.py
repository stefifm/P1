import random

print("Funciones para el programa sobre barcos")

class Barco:
    def __init__(self, pat, emp, tipo, dias):
        self.patente = pat
        self.empresa = emp
        self.tipo = tipo
        self.dias = dias

def to_string(barco):
    r = " "
    r += "Patente del barco: " + barco.patente
    r += " - Empresa: " + barco.empresa
    r += " - Tipo de carga: " + str(barco.tipo)
    r += " - Cantidad de días: " + str(barco.dias)
    return r

#------------------------------------------------------------------------------

#opcion 1
def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. El valor debe ser mayor a cero")
    return n

def carga_automatica(barco):
    pat = ("ABC", "HFG", "LEC", "HAM", "VER", "VET", "GRO")
    emp = ("CARS SA", "DHL", "FEDEX", "APPLE", "UPS", "MI6")
    for i in range(len(barco)):
        patente = random.choice(pat)
        empresa = random.choice(emp)
        tipo = random.randint(0, 14)
        dias = random.randint(1, 30)
        b = Barco(patente, empresa, tipo, dias)
        barco[i] = b
    return barco

def opcion1(barco):
    print("Hora de cargar el arreglo. Presione <Enter< para continuar")
    input()
    carga_automatica(barco)
    print("Hecho. El arrgelo ya está cargado")

#opcion2
def orden_sort(barco):
    n = len(barco)
    for i in range(n-1):
        for j in range(i+1, n):
            if barco[i].patente < barco[j].patente:
                barco[i], barco[j] = barco[j], barco[i]

def display(barco):
    for i in range(len(barco)):
        print(to_string(barco[i]))

def opcion2(barco):
    if barco[0] == None:
        print("El arrelo no se ha cargado")
        return
    orden_sort(barco)
    display(barco)

#opcion3
def contador(barco):
    cont_carga = [0] * 15
    for i in range(len(barco)):
        c = int(barco[i].tipo)
        cont_carga[c] += 1
    for i in range(15):
        if cont_carga != 0:
            print("Tipo de carga",i,"Cantidad de barcos",cont_carga[i])

def opcion3(barco):
    if barco[0] == None:
        print("El arrelo no se ha cargado")
        return
    contador(barco)

#opcion4
def menor_dia(barco):
    menor = barco[0]
    for i in range(len(barco)):
        if barco[i].tipo == 0 or barco[i].tipo == 1 or barco[i].tipo == 2:
            if barco[i].dias < menor.dias:
                menor = barco[i]
    return menor

def opcion4(barco):
    if barco[0] == None:
        print("El arrelo no se ha cargado")
        return
    menor = menor_dia(barco)
    print("El barco",menor.patente, "de los tipos 0, 1 o 2 es el que menos "
                                    "días lleva, es decir, lleva:",menor.dias)

#opcion5

def buscar(emp, tip ,barco):
    for i in range(len(barco)):
        if barco[i].empresa == emp and barco[i].tipo == tip:
            return barco[i]
    return None

def opcion5(barco):
    if barco[0] == None:
        print("El arrelo no se ha cargado")
        return
    emp = input("Ingrese el nombre de la empresa que busca: ")
    tip = 8
    bar = buscar(emp, tip,barco)
    if bar != None:
        print("Datos encontrados")
        print(to_string(bar))
    else:
        print("Datos encontrados")
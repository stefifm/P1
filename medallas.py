import random

print("Funciones para el medallero")

class Pais:
    def __init__(self, nom, continente, oro, plata, bronce):
        self.nombre = nom
        self.continente = continente
        self.oro = oro
        self.plata = plata
        self.bronce = bronce
        self.total = oro + plata + bronce

def to_string(pais):
    r = " "
    r += "Nombre del país participante: " + pais.nombre
    r += " - Continente: " + str(pais.continente)
    r += "- Oro: " + str(pais.oro)
    r += "- Plata: " + str(pais.plata)
    r += "- Bronce: " + str(pais.bronce)
    r += "- Total de medallas: " + str(pais.total)
    return r
#------------------------------------------------------------------------------

#opcion 1
def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. No debe ser menor o igual a", inf)
    return n

def carga_automatica(pais):
    nom = ("Pais1", "Pais2", "Pais3", "Pais4", "Pais5", "Pais6", "Pais7",
           "Pais8", "Pais9", "Pais10")
    for i in range(len(pais)):
        nombre = random.choice(nom)
        continente = random.randint(0, 4)
        oro = random.randint(1, 50)
        plata = random.randint(1, 50)
        bronce = random.randint(1, 50)
        p = Pais(nombre, continente, oro, plata, bronce)
        pais[i] = p
    return pais

def orden_sort(pais):
    n = len(pais)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pais[i].total < pais[j].total:
                pais[i], pais[j] = pais[j], pais[i]

def display(pais):
    for i in range(len(pais)):
        print(to_string(pais[i]))

def opcion1(pais):
    print("Muestra ordenada de la lista de participantes...")
    orden_sort(pais)
    display(pais)

#opcion 2
def promedio_oro(pais, continente):
    contador = 0
    acumulador = 0
    for i in range(len(pais)):
        if pais[i].continente == continente:
            contador += 1
            acumulador += pais[i].oro
    if contador > 0:
        prom = round(acumulador / contador, 2)
        print("El promedio de medallas de oro del continente",continente,
              "es de:",prom)
#Acá debería haber una validacion del rango en la búsqueda del continente
def opcion2(pais):
    if pais[0] == None:
        print("El arreglo no se ha cargado")
        return
    conti = int(input("Ingrese el número del continente para el cálculo de "
                      "promedio de medallas de oro: "))
    promedio_oro(pais, conti)

#opcion 3

def mayor_plata(pais):
    # mayor = pais[0]
    # mayores = []
    # for i in range(len(pais)):
    #     if pais[i].plata > mayor.plata:
    #         mayor = pais[i]
    #         mayores.append(pais[i])
    #
    # # for i in range(len(pais)):
    # #     if pais[i].plata == mayor:
    # #         mayores.append(pais[i])
    mayor = None
    for i in pais:
        if mayor is None or i.plata > mayor:
            mayor = i.plata
    mayores = []
    for j in pais:
        if j.plata == mayor:
            mayores.append(j)
    return mayores

def opcion3(pais):
    if pais[0] == None:
        print("El arreglo no se ha cargado")
        return
    mayor = mayor_plata(pais)
    display(mayor)


#opcion 4
def solo_bronce(pais):
    cont_bronce = 0
    for i in range(len(pais)):
        if pais[i].bronce > 0 and pais[i].oro == 0 and pais[i].plata == 0:
            cont_bronce += 1
    return cont_bronce

def opcion4(pais):
    if pais[0] == None:
        print("El arreglo no se ha cargado")
        return
    bronce = solo_bronce(pais)
    porcentaje_bronce = round(bronce * 100 / len(pais), 2)
    print("Cantidad de países con solo medallas de bronce:",bronce)
    print("Porcentaje sobre el total:",porcentaje_bronce,"%")

#opcion5
def contador_continente(pais):
    cont_conti = [0] * 5
    for i in range(len(pais)):
        c = int(pais[i].continente)
        cont_conti[c] += 1
    for i in range(5):
        if cont_conti[i] > 0:
            print("Continente:",i,"Cantidad de países:",cont_conti[i])

def opcion5(pais):
    if pais[0] == None:
        print("El arreglo no se ha cargado")
        return
    contador_continente(pais)
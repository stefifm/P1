import random
print("funcion para comercio de deportes")


class Comercio:
    def __init__(self, num, descripcion, costo, sport):
        self.numero = num
        self.descripcion = descripcion
        self.costo = costo
        self.deporte = sport



def to_string(comercio):
    r = " "
    r += "Número identificador: " + str(comercio.numero)
    r += " - Descripción:" + str(comercio.descripcion)
    r += " - Costo: " + str(comercio.costo)
    r += " - Deporte: " + str(comercio.deporte)
    return r


#opcion 1

def validar(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error. No debe ser menor o igual a", inf)
    return n

def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Valor no válido. Ingrese un valor entre",str(inf),"y",
                  str(sup))
    return n

def carga_manual(comercio):
    for i in range(len(comercio)):
        numero = random.randint(1000, 7000)
        descripcion = random.randint(100, 600)
        costo = random.randint(50, 1000)
        deporte = random.randint(1, 15)
        reg1 = Comercio(numero, descripcion, costo, deporte)
        comercio[i] = reg1
    return comercio

def opcion1(comercio):
    print("Cargue el arreglo")
    carga_manual(comercio)

#opcion 2
def orden_sort(comercio):
    # algoritmo de selección directa
    n = len(comercio)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if comercio[i].numero > comercio[j].numero:
                comercio[i], comercio[j] = comercio[j], \
                                           comercio[i]


def display(comercio):
    for i in range(len(comercio)):
        print(to_string(comercio[i]))


def opcion2(comercio):
    if comercio[0] == None:
        print("El arreglo no se ha cargado")
        return
    orden_sort(comercio)
    display(comercio)

#opcion3
# def promedio(comercio, c):
#     acum = 0
#     cont = 0
#     for i in comercio:
#         if i.costo > c:
#             cont += 1
#             acum += i.costo
#             print(to_string(i))
#     if cont > 0:
#         prom = round(acum / cont, 2)
#         print("El promedio es de:",prom)

def costo_mayores_valor(comercio, c):
    contador = 0
    acumulador = 0
    for i in range(len(comercio)):
        if comercio[i].costo > c:
            contador += 1
            acumulador += comercio[i].costo
            print(to_string(comercio[i]))
    if contador > 0:
        prom = round(acumulador / contador, 2)
        print("El promedio de productos mayores a c es: ",prom)

def opcion3(comercio):
    if comercio[0] == None:
        print("El arreglo no se ha cargado")
        return
    c = int(input("Ingrese el costo a buscar: "))
    costo_mayores_valor(comercio,c)


#opcion4
def buscar_descripcion(comercio, d):
    for i in range(len(comercio)):
        if comercio[i].descripcion == d:
            return comercio[i]
    return None

def opcion4(comercio):
    if comercio[0] == None:
        print("El arreglo no se ha cargado")
        return
    d = int(input("Cargue la descripción a buscar: "))
    desc = buscar_descripcion(comercio, d)
    if desc != None:
        print("Datos de la descripción del artículo encontrado:")
        print(to_string(desc))
    else:
        print("Esa descripción no fue cargada o no se encuentra")

#opcion 5
def vec_acumulado(comercio):
    vec_acu = [0] * 15
    for i in range(len(comercio)):
        d = int(comercio[i].deporte) - 1
        vec_acu[d] += comercio[i].costo
    for i in range(15):
        if vec_acu[i] != 0:
            print("Artículo:", i + 1, "Costo acumulado:", vec_acu[i])

def opcion5(comercio):
    if comercio[0] == None:
        print("El arreglo no se ha cargado")
        return
    vec_acumulado(comercio)




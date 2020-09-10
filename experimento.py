print("experimento con format")


nom = "Stefania Bruera"
edad = 28
materia = "AED"

cad1 = "{:<6}".format("Nombre: " + nom)
cad1 += "{:<10}".format("\t- Edad: " + str(edad))
cad1 += "{:<10}".format(" - Materia: " + materia)

print(cad1)
import random

class Nodo:
    def __init__(self, calidad, tiempo, tipo, longitud, status):
        self.calidad = calidad
        self.tiempo = tiempo
        self.tipo = tipo
        self.longitud = longitud
        self.status = status


def tiempo(tiempo):
    resul = tiempo / 3600 * 100
    return int(resul)
    
def longitud(longitud):
    resul = longitud / 90000 * 100
    return int(resul)


caminos = [[], [], []]
tipoList = [25, 50, 75, 100]

for element in caminos:
    x = random.randrange(1, 99)
    for item in range(x):
        cal = random.randrange(1, 100)
        tie = random.randrange(1, 3600)
        tieFinal = tiempo(tie)
        tip = random.choice(tipoList)
        lon = random.randrange(1, 90000)
        lonFinal = longitud(lon)
        sta = random.randrange(1, 100)
        element.append(Nodo(cal, tieFinal, tip, lonFinal, sta))


caminosFinal = [0,0,0]
cont = 0
w = 0

for idx, element in enumerate(caminos):
    cont=0
    w = random.randrange(1,100)
    for item in element:
        cont += item.calidad
        cont += item.tiempo
        cont += item.tipo
        cont += item.longitud
        cont += item.status
        cont += w
    caminosFinal[idx] = cont
        


print("Camino más corto " + str(caminosFinal.index(min(caminosFinal))) + " con " + str(min(caminosFinal)))
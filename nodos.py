import random

class Nodo:
    def __init__(self, calidad, tiempo, tipo, longitud, status):
        self.calidad = calidad
        self.tiempo = tiempo
        self.tipo = tipo
        self.longitud = longitud
        self.status = status


caminos = [[], [], []]
tipoList = [25, 50, 75, 100]

for element in caminos:
    x = random.randrange(1, 99)
    for item in range(x):
        cal = random.randrange(1, 100)
        tie = random.randrange(1, 3600)
        tip = random.choice(tipoList)
        lon = random.randrange(1, 90000)
        sta = random.randrange(1, 100)
        element.append(Nodo(cal, tie, tip, lon, sta))


caminosFinal = [0,0,0]
cont = 0

for idx, element in enumerate(caminos):
    cont=0
    for item in element:
        cont+=item.calidad
        cont+=item.tiempo
        cont+=item.tipo
        cont+=item.longitud
        cont+=item.status
    caminosFinal[idx] = cont
        

print(caminosFinal)
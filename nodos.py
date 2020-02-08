import random
from funciones import *
import json

caminos = [[]]
tipoList = [25, 50, 75, 100]
caminosFinal = [0,0,0]
cont = 0
w = 0

class Camino:
    def __init__(self, complejidad, tiempo, tipo, longitud, status):
        self.complejidad    = complejidad
        self.tiempo         = tiempo
        self.tipo           = tipo
        self.longitud       = longitud
        self.status         = status

class Carro:
    def __init__(self, velocidad, calCarro, staCarro, tipLlanta, staLlanta, 
     gasCantidad, cilindraje, pesoTotal, aerodinamica, staAceite, tempMotor, batalla):
        self.velocidad = velocidad
        self.calCarro = calCarro
        self.staCarro = staCarro
        self.tipLlanta = tipLlanta
        self.staLlanta = staLlanta 
        self.gasCantidad = gasCantidad
        self.cilindraje = cilindraje
        self.pesoTotal = pesoTotal
        self.aerodinamica = aerodinamica
        self.staAceite = staAceite
        self.tempMotor = tempMotor
        self.batalla = batalla




carVel = 110       # Velocidad se calula en m/s y km/h velocidad maxima 110 Km/h, según la complejidad de las curvas puede bajar a un minimo de 60 km/h
carCalCarro = 100     # 100 alta, 75 media, menos de 50 baja
carStaCarro = 100     # 100 buen estado, 75 estado normal, 50 mal estado
carTipLLanta = 100    # 100 radial menos combustible, 50 HP mayor velocidad mayor adeherencia mas combustible
carStaLLanta = 100 # 100 buen estado, 75 estado normal, 50 mal estado
carGasCantidad = 65# maximo de 65 litros
carCilindros = 8      # numero de cilindros, mientras más cilindros más gasolina gasta
carPeso = 1500        # peso en Kg, mientras más pesado mayor consumo de gasolina y mayor disminución de velocidad en curvas
carAero = 100         # mientras más alto sea el número menos resistencia al viento, por lo tanto mayor velocidad
carStaAce = 100    # mientras mejor sea el estado del aceite menos se calienta el motor
carTempMotor = 90  # temperatura en grados celsius, mientras más alto sea el estado del aceite menos tiende a calentarse, maximo de 150 grados, nunca baja de 70
carBatalla = 4.3      # Distancia entre ejes, mientras mayor sea la distancia mayor estabilidad en cruvas




for element in caminos:
    x = random.randrange(1, 99)
    for item in range(x):
        cal = random.randrange(1, 100)
        tieFinal = 0
        tip = random.choice(tipoList)
        lon = random.randrange(1, 90000)
        lonFinal = longitud(lon)
        sta = random.randrange(1, 100)
        element.append(Camino(cal, tieFinal, tip, lonFinal, sta))

for idx, element in enumerate(caminos):
    cont=0
    w = random.randrange(1,100)
    for item in element:
        cont += item.complejidad
        cont += item.tiempo
        cont += item.tipo
        cont += item.longitud
        cont += item.status
        cont += w
    caminosFinal[idx] = cont
        

carro1 = Carro(velocidad(carVel), carCalCarro, carStaCarro, carTipLLanta, carStaLLanta, 
gasolina(carGasCantidad), carCilindros, peso(carPeso), carAero, carStaAce, carTempMotor, batalla(carBatalla))


velMax = carro1.velocidad
for item in caminos[0]:
    newVel = changeVelocidad(velMax, item.complejidad, item.tipo, item.status, carro1.tipLlanta, carro1.staLlanta, 
    carro1.pesoTotal, carro1.aerodinamica, carro1.batalla, item.longitud)
    newStaLLanta = changeStaLLanta(carro1.staLlanta, item.tipo, item.status, item.longitud)
    newGas = changeGas(carro1.gasCantidad, item.longitud, carro1.cilindraje)
    carro1.staLlanta = newStaLLanta
    carro1.gasCantidad = newGas

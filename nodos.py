import random
from funciones import *
import math

caminos = [[]]
tipoList = [25, 50, 75, 100]
caminosFinal = [0,0,0]
cont = 0
w = 0
carroLista = []
eventos = []

class Camino:
    def __init__(self, complejidad, tiempo, tipo, longitud, status, precipitaciones, viento, dirViento, neblina):
        self.complejidad    = complejidad
        self.tiempo         = tiempo
        self.tipo           = tipo
        self.longitud       = longitud
        self.status         = status
        self.precipitaciones= precipitaciones
        self.viento         = viento
        self.dirViento      = dirViento
        self.neblina        = neblina

class Carro:
    def __init__(self, velocidad, calCarro, staCarro, tipLlanta, staLlanta, 
     gasCantidad, cilindraje, pesoTotal, aerodinamica, staAceite, tempMotor,
    batalla, dinero, refaccion, ponchado):
        self.velocidad      = velocidad
        self.calCarro       = calCarro
        self.staCarro       = staCarro
        self.tipLlanta      = tipLlanta
        self.staLlanta      = staLlanta 
        self.gasCantidad    = gasCantidad
        self.cilindraje     = cilindraje
        self.pesoTotal      = pesoTotal
        self.aerodinamica   = aerodinamica
        self.staAceite      = staAceite
        self.tempMotor      = tempMotor
        self.batalla        = batalla
        self.dinero         = dinero
        self.refaccion      = refaccion
        self.ponchado       = ponchado




carVel = 90       # Velocidad se calula en m/s y km/h velocidad maxima 110 Km/h, según la complejidad de las curvas puede bajar a un minimo de 60 km/h
carCalCarro = 100     # 100 alta, 75 media, menos de 50 baja
carStaCarro = 100     # 100 buen estado, 75 estado normal, 50 mal estado
carTipLLanta = 100    # 100 radial menos combustible, 50 HP mayor velocidad mayor adeherencia mas combustible
carStaLLanta = 100 # 100 buen estado, 75 estado normal, 50 mal estado
carGasCantidad = 65# maximo de 65 litros
carCilindros = 8      # numero de cilindros, mientras más cilindros más gasolina gasta
carPeso = 1500        # peso en Kg, mientras más pesado mayor consumo de gasolina y mayor disminución de velocidad en curvas
carAero = 100         # mientras más alto sea el número menos resistencia al viento, por lo tanto mayor velocidad
carStaAce = 100    # mientras mejor sea el estado del aceite menos se calienta el motor
carTempMotor = 100  # temperatura en grados celsius, mientras más alto sea el estado del aceite menos tiende a calentarse, maximo de 150 grados, nunca baja de 70
carBatalla = 4.3      # Distancia entre ejes, mientras mayor sea la distancia mayor estabilidad en cruvas
carDinero = 3000
carRef = True
carPonch = False



for element in caminos:
    x = random.randrange(1, 99)
    for item in range(x):
        cal = random.randrange(1, 100)
        tieFinal = 0
        tip = random.choice(tipoList)
        lon = random.randrange(1, 90000)
        lonFinal = longitud(lon)
        sta = random.randrange(1, 100)
        preci = random.randrange(1,100)
        vien = random.randrange(1, 100)
        dirvien = random.choice([True, False])
        neblina = random.randrange(1, 100)
        element.append(Camino(cal, tieFinal, tip, lonFinal, sta, preci, vien, dirvien, neblina))

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
gasolina(carGasCantidad), carCilindros, peso(carPeso), carAero, carStaAce, carTempMotor, 
batalla(carBatalla), carDinero, carRef, carPonch)

newVel = carro1.velocidad
for idx, item in enumerate(caminos[0]):
    if carro1.gasCantidad<=0:
        break
    
    



    evento = ""
    newVel              = changeVelocidad(newVel, item.complejidad, item.tipo, item.status, carro1.tipLlanta, carro1.staLlanta, 
                        carro1.pesoTotal, carro1.aerodinamica, carro1.batalla, item.longitud, item.precipitaciones, item.viento, 
                        item.dirViento, item.neblina)
    newStaLLanta        = changeStaLLanta(carro1.staLlanta, item.tipo, item.status, item.longitud, item.precipitaciones)
    newGas              = changeGas(carro1.gasCantidad, item.longitud, carro1.cilindraje)
    newAceite           = changeAceite(carro1.staAceite, item.longitud, carro1.tempMotor)
    carro1.staLlanta    = newStaLLanta
    carro1.gasCantidad  = newGas
    carro1.velocidad    = newVel
    carro1.staAceite    = newAceite
    item.tiempo         = math.ceil(item.longitud / carro1.velocidad)
    

    if gasolinera(item.complejidad):
        evento += "Gasolinera. "
        if carro1.gasCantidad < 10:
            carro1.gasCantidad = gasolina(65)

    if reten(carro1.velocidad, carro1.calCarro, item.complejidad):
        evento += "Reten. "
        if carro1.calCarro > 75:
            carro1.dinero -= 200

    if poncharse(carro1.staLlanta):
        evento += "Ponchado. "
        carro1.ponchado = True
        if carro1.refaccion:
            evento += "LLanta cambiada"
            carro1.refaccion = False
            carro1.ponchado = False
            carro1.staLlanta = 100

    # if desponchadora(item.status):

        
            

    

    carroLista.append(Carro(newVel, carro1.calCarro, carro1.staCarro, carro1.tipLlanta, carro1.staLlanta, carro1.gasCantidad, 
        carro1.cilindraje, carro1.pesoTotal, carro1.aerodinamica, carro1.staAceite, carro1.tempMotor, carro1.batalla,
        carro1.dinero, carro1.refaccion, carro1.ponchado))


    eventos.append(evento)

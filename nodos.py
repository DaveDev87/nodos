import random
from funciones import *
import math
from eventos import newCarro
import json

caminos = [[]]
tipoList = [25, 50, 75, 100]
caminosFinal = [0,0,0]
cont = 0
w = 0
carroLista = []
eventos = []

content = ""

with open("data.txt", "r") as f:
    content = f.read()


gasLIst = []
for item in json.loads(content):
    gas = list(filter(lambda x: x["evento"]=="gasolinera", item))
    gasLIst += gas

print(gasLIst[0])



# print(json.loads(content)[0])
# for i in json.loads(content):
#     print(i)


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
    batalla, dinero):
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



for element in caminos: # GENERACION DE CAMINOS
    x = random.randrange(0, 10)
    for item in range(100):# GENERACION DE NODOS 
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

carro1 = Carro(int(velocidad(carVel)), carCalCarro, carStaCarro, carTipLLanta, carStaLLanta, 
gasolina(carGasCantidad), carCilindros, peso(carPeso), carAero, carStaAce, carTempMotor, 
int(batalla(carBatalla)), carDinero)

newVel = carro1.velocidad
for idx, item in enumerate(caminos[0]):
    
    
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
    
    
                
    CarEvent = newCarro(item.complejidad, int(newVel), int(carro1.calCarro), int(item.status), item.tipo, item.precipitaciones, carro1.tempMotor, carro1.staAceite, item.neblina, item.longitud, item.viento, int(carro1.staLlanta), carro1.batalla, carro1.dinero, item.dirViento, carro1.pesoTotal, carro1.cilindraje, item.tiempo, carro1.aerodinamica, carro1.staCarro, carro1.tipLlanta, carro1.gasCantidad)
    if CarEvent[0]==False or CarEvent[2].velocidad<=0 or CarEvent[2].staLlanta<=0 or CarEvent[2].staCarro<=0:
        break
    
        
    carro1 = CarEvent[2]
    carroLista.append(CarEvent[1])



# with open("data.txt", "w",encoding="utf-8") as f:
#     json.dump(carroLista, f, ensure_ascii=False, indent=4)
    
    


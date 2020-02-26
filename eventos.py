import random
from funciones import promedio

class Carro2:
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

def gasolinera(complejidad):
    ra = random.randrange(1, 100)
    if(ra<complejidad):
        triggered = True
    else:
        triggered = False
    return {
        "evento": "gasolinera",
        "triggered": triggered,
        "complejidad": complejidad,
        "refuerzo": "Positivo"
        }

def reten(velocidad, calidad, complejidad, dinero):
    ra = random.randrange(1, 100)
    cof = 20 
    resul = promedio(cof, velocidad) + promedio(cof, complejidad)
    if(ra<resul):
        triggered = True
    else:
        triggered = False
    return {
        "evento": "reten",
        "triggered": triggered,
        "complejidad": complejidad,
        "calidad": calidad,
        "velocidad": velocidad,
        "dinero": dinero,
        "refuerzo": "Negativo"
        }

def poncharse(status):
    ra = random.randrange(1, 100)
    if(ra<status/4):
         triggered = True
    else:
        triggered = False
    return {
        "evento": "poncharse",
        "triggered": triggered,
        "staLLanta": status,
        "refuerzo": "Negativo"
        }

def desponchadora(tipo):
    ra = random.randrange(1, 100)
    if ra < tipo:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "desponchadora",
        "triggered": triggered,
        "tipo": tipo,
        "refuerzo": "Positivo"
        }

def bateria(precipitaciones, tempMotor):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, tempMotor)
    resul = cof/2
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "bateria",
        "triggered": triggered,
        "precipitaciones": precipitaciones,
        "tempMotor": tempMotor,
        "refuerzo": "Negativo"
        }

def calentamientoMotor(tempMotor, aceite, status):
    ra = random.randrange(1, 100)
    cof = promedio(100, tempMotor) + promedio(100, aceite) + promedio(100, status)
    resul = cof / 3
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "sobrecalentamiento",
        "triggered": triggered,
        "tempMotor": tempMotor,
        "aceite": aceite,
        "status": status,
        "refuerzo": "Negativo"
        }

def aguaMotor(precipitaciones, neblina):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, neblina)
    resul = cof / 2
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "aguaMotor",
        "triggered": triggered,
        "precipitaciones": precipitaciones,
        "neblina": neblina,
        "refuerzo": "Negativo"
        }

def taller(complejidad):
    ra = random.randrange(1, 100)
    if ra < complejidad:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "taller",
        "triggered": triggered,
        "complejidad": complejidad,
        "refuerzo": "Positivo"
        }

def animales(longitud, tipo, precipitaciones):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, longitud)
    resul = cof / 2
    if ra < resul:
         triggered = True
    else:
        triggered = False
    return {
        "evento": "animales",
        "triggered": triggered,
        "longitud": longitud,
        "tipo": tipo,
        "precipitaciones": precipitaciones,
        "refuerzo": "Negativo"
        }

def choque(complejidad, status, precipitaciones, viento, neblina, velocidad, stallanta, batalla):
    ra = random.randrange(1, 100)
    cof = promedio(100, complejidad) + promedio(100, status) + promedio(100, precipitaciones) + promedio(100, viento) + promedio(100, neblina) + promedio(100, stallanta) + promedio(100, batalla)
    resul = cof / 12
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "choque",
        "triggered": triggered,
        "complejidad": complejidad,
        "statusCar": status,
        "precipitaciones": precipitaciones,
        "viento": viento,
        "neblina": neblina,
        "velocidad": velocidad,
        "status": stallanta,
        "batalla": batalla,
        "refuerzo": "Negativo"
        }

def lluvia(precipitaciones, viento):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, viento)
    resul = cof / 2
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "lluvia",
        "triggered": triggered,
        "precipitaciones": precipitaciones,
        "viento": viento,
        "refuerzo": "Negativo"
        }

def tormenta(precipitaciones, viento):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, viento)
    resul = cof /1.3
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "tormenta",
        "triggered": triggered,
        "precipitaciones": precipitaciones,
        "viento": viento,
        "refuerzo": "Negativo"
        }

def rayo(batalla):
    ra = random.randrange(1, 5)
    resul = batalla
    if ra > resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "rayo",
        "triggered": triggered,
        "batalla": batalla,
        "refuerzo": "Negativo"
        }

def visibilidad(neblina):
    ra = random.randrange(1, 5)
    resul = neblina
    if ra > resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "visibilidad",
        "triggered": triggered,
        "neblina": neblina,
        "refuerzo": "Negativo"
        }

def fantasmas(neblina, compania):
    ra = random.randrange(1, 5)
    resul = neblina + compania
    if ra > resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "fantasmas",
        "triggered": triggered,
        "neblina": neblina,
        "refuerzo": "Negativo"
        }

def tesoro(trigger, dinero):
    ra = random.randrange(1, 50)
    comp = 100
    if trigger == True:
        comp = 50
    if ra < comp:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "tesoro",
        "triggered": triggered,
        "dinero": dinero,
        "refuerzo": "Positivo"
        }

def aventon(neblina, precipitaciones):
    ra = random.randrange(1, 50)
    cof = promedio(100, neblina) + promedio(100, precipitaciones)
    resul = cof / 3
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "aventon",
        "triggered": triggered,
        "precipitaciones": precipitaciones,
        "neblina": neblina,
        "refuerzo": "Positivo"
        }

def trafico(complejidad, status):
    ra = random.randrange(1, 50)
    cof = promedio(100, complejidad) + promedio(100, status)
    resul = cof / 3
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "aguaMotor",
        "triggered": triggered,
        "complejidad": complejidad,
        "status": status,
        "refuerzo": "Positivo"
        }

def ave(viento, dirviento):
    ra = random.randrange(1, 50)
    if dirviento:
        ra=ra*0.2
    cof = viento*2
    if ra < cof:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "ave",
        "triggered": triggered,
        "viento": viento,
        "dirviento": dirviento,
        "refuerzo": "Negativo"
        }

def elevacion(peso, cilindraje):
    ra = random.randrange(1, 50)

    resul = promedio(100, peso) / cilindraje
    if ra < resul:
        triggered = True
    else:
        triggered = False
    return {
        "evento": "elevacion",
        "triggered": triggered,
        "peso": peso,
        "cilindraje": cilindraje,
        "refuerzo": "Negativo"
        }

#TRIGGER DE EVENTOS

def newCarro(complejidad, velocidad, calidad, status, tipo, precipitaciones, tempMotor, aceite, neblina, longitud, viento, staLLanta, batalla, dinero, dirViento, peso, cilindraje, tiempo, aerodinamica, staCarro, tipoLLanta, gasCantidad):
    eventos = []
    continua = True
    treas = False

    N_velocidad = velocidad 
    N_tempMotor = tempMotor 
    N_aceite = aceite 
    N_staLLanta = staLLanta 
    N_dinero = dinero 
    N_gasCantidad= gasCantidad 



    gasolineraEvent = gasolinera(complejidad)
    retenEvent = reten(velocidad, calidad, complejidad, dinero)
    desponchadoraEvent = desponchadora(tipo)
    tallerEvent = taller(complejidad)
    poncharseEvent = poncharse(staLLanta)
    bateriaEvent = bateria(precipitaciones, tempMotor)
    calentamientoMotorEvent = calentamientoMotor(tempMotor, aceite, status)
    aguaMotorEvent = aguaMotor(precipitaciones, neblina)
    animalesEvent = animales(longitud, tipo, precipitaciones)
    choqueEvent = choque(complejidad, status, precipitaciones, viento, neblina, velocidad, staLLanta, batalla)
    lluviaEvent = lluvia(precipitaciones, viento)
    tormentaEvent = tormenta(precipitaciones, viento)
    rayoEvent = rayo(batalla)
    visibilidadEvent = visibilidad(neblina)
    fantasmasEvent = fantasmas(neblina, 30)
    tesoroEvent = tesoro(treas, dinero)
    aventonEvent = aventon(neblina, precipitaciones)
    traficoEvent = trafico(complejidad, status)
    aveEvent = ave(viento, dirViento)
    elevacionEvent = elevacion(peso, cilindraje)

    eventosData = [gasolineraEvent, retenEvent, desponchadoraEvent, tallerEvent, poncharseEvent, bateriaEvent, calentamientoMotorEvent, aguaMotorEvent,
    animalesEvent, choqueEvent, lluviaEvent, tormentaEvent, rayoEvent, visibilidadEvent, fantasmasEvent, tesoroEvent, aventonEvent, traficoEvent, aveEvent, elevacionEvent]

    if gasolineraEvent["triggered"]==True:
        eventos.append("Gasolinera")
        if gasCantidad<=10:
            N_gasCantidad = 100
    
    if retenEvent["triggered"]==True:
        eventos.append("Reten")
        if dinero<=0:
            continua = False
        elif calidad>70:
            N_dinero-=30
        else:
            N_dinero-=5

    if desponchadoraEvent["triggered"]==True:
        eventos.append("Desponchadora")

    if tallerEvent["triggered"]==True:
        eventos.append("Taller")

    if poncharseEvent["triggered"]==True:
        eventos.append("Ponchado")
        if "Desponchadora" in eventos == False:
            continua = False

    if bateriaEvent["triggered"]==True:
        eventos.append("Fallo de bateria")
        if "Taller" in eventos == False:
            continua = False

    if calentamientoMotorEvent["triggered"]==True:
        eventos.append("Sobrecalentamiento del motor")
        N_aceite -= 12

    if aguaMotorEvent["triggered"]==True:
        eventos.append("Agua en el motor")

    if animalesEvent["triggered"]==True:
        eventos.append("Choque con animal")
        if "Taller" in eventos == False:
            continua = False

    if choqueEvent["triggered"]==True:
        eventos.append("Choque")
        if "Taller" in eventos == False:
            continua = False

    if lluviaEvent["triggered"]==True:
        eventos.append("Lluvias torrenciales")
        N_velocidad -= 10
        N_tempMotor -= 2

    if tormentaEvent["triggered"]==True:
        eventos.append("Tormenta electrica")
        N_velocidad -= 15
        N_staLLanta -= 9
    
    if rayoEvent["triggered"]==True:
        eventos.append("Impacto de rayo")
        if "Taller" in eventos == False:
            continua = False
    
    if visibilidadEvent["triggered"]==True:
        eventos.append("Perdida de visibilidad")
        N_velocidad -= 7

    if fantasmasEvent["triggered"]==True:
        eventos.append("Fantasma")
        treas = True

    if tesoroEvent["triggered"]==True:
        eventos.append("Tesoro")
        N_dinero += 4000

    if aventonEvent["triggered"]==True:
        eventos.append("Aventon")
        N_dinero += 500

    if traficoEvent["triggered"]==True:
        eventos.append("Trafico")
        N_velocidad -= 10
        N_gasCantidad -= 8

    if aveEvent["triggered"]==True:
        eventos.append("Ave en el parabrisas")
        N_velocidad -= 5

    if elevacionEvent["triggered"]==True:
        eventos.append("Varado por peso")
        N_gasCantidad -= 12
        N_velocidad -= 12
        N_tempMotor += 5

    return [continua, eventosData, Carro2(int(N_velocidad), calidad, staCarro, tipoLLanta, N_staLLanta, N_gasCantidad, cilindraje, peso, aerodinamica, aceite, N_tempMotor, batalla, N_dinero)]
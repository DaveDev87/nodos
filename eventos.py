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
        return {
            "evento": "gasolinera",
            "complejidad": complejidad,
            "refuerzo": "Positivo"
            }
    else:
        return False

def reten(velocidad, calidad, complejidad, dinero):
    ra = random.randrange(1, 100)
    cof = 20 
    resul = promedio(cof, velocidad) + promedio(cof, complejidad)
    if(ra<resul):
        return True
    else:
        return False

def poncharse(status):
    ra = random.randrange(1, 100)
    if(ra<status/4):
        return True
    else:
        return False

def desponchadora(tipo):
    ra = random.randrange(1, 100)
    if ra < tipo:
        return True
    else:
        return False

def bateria(precipitaciones, tempMotor):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, tempMotor)
    resul = cof/2
    if ra < resul:
        return True
    else:
        return False

def calentamientoMotor(tempMotor, aceite, status):
    ra = random.randrange(1, 100)
    cof = promedio(100, tempMotor) + promedio(100, aceite) + promedio(100, status)
    resul = cof / 3
    if ra < resul:
        return True
    else:
        return False

def aguaMotor(precipitaciones, neblina):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, neblina)
    resul = cof / 2
    if ra < resul:
        return True
    else:
        return False

def taller(complejidad):
    ra = random.randrange(1, 100)
    if ra < complejidad:
        return True
    else:
        return False

def animales(longitud, tipo, precipitaciones):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, longitud)
    resul = cof / 2
    if ra < resul:
        return True
    else:
        return False

def choque(complejidad, status, precipitaciones, viento, neblina, velocidad, stallanta, batalla):
    ra = random.randrange(1, 100)
    cof = promedio(100, complejidad) + promedio(100, status) + promedio(100, precipitaciones) + promedio(100, viento) + promedio(100, neblina) + promedio(100, stallanta) + promedio(100, batalla)
    resul = cof / 12
    if ra < resul:
        return True
    else:
        return False

def lluvia(precipitaciones, viento):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, viento)
    resul = cof / 2
    if ra < resul:
        return True
    else:
        return False

def tormenta(precipitaciones, viento):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, viento)
    resul = cof /1.3
    if ra < resul:
        return True
    else:
        return False

def rayo(batalla):
    ra = random.randrange(1, 5)
    resul = batalla
    if ra > resul:
        return True
    else:
        return False

def visibilidad(neblina):
    ra = random.randrange(1, 5)
    resul = neblina
    if ra > resul:
        return True
    else:
        return False

def fantasmas(neblina, compania):
    ra = random.randrange(1, 5)
    resul = neblina + compania
    if ra > resul:
        return True
    else:
        return False

def tesoro(trigger):
    ra = random.randrange(1, 50)
    comp = 100
    if trigger == True:
        comp = 50
    if ra < comp:
        return True
    else:
        return False

def aventon(neblina, precipitaciones):
    ra = random.randrange(1, 50)
    cof = promedio(100, neblina) + promedio(100, precipitaciones)
    resul = cof / 3
    if ra < resul:
        return True
    else:
        return False

def trafico(complejidad, status):
    ra = random.randrange(1, 50)
    cof = promedio(100, complejidad) + promedio(100, status)
    resul = cof / 3
    if ra < resul:
        return True
    else:
        return False

def ave(viento, dirviento):
    ra = random.randrange(1, 50)
    if dirviento:
        ra=ra*0.2
    cof = viento*2
    if ra < cof:
        return True
    else:
        return False

def elevacion(peso, cilindraje):
    ra = random.randrange(1, 50)

    resul = promedio(100, peso) / cilindraje
    if ra < resul:
        return True
    else:
        return False

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


    if gasolinera(complejidad)==True:
        eventos.append("Gasolinera")
        if gasCantidad<=10:
            N_gasCantidad = 100
    
    if reten(velocidad, calidad, complejidad, dinero)==True:
        eventos.append("Reten")
        if dinero<=0:
            continua = False
        elif calidad>70:
            N_dinero-=30
        else:
            N_dinero-=5

    if desponchadora(tipo)==True:
        eventos.append("Desponchadora")

    if taller(complejidad)==True:
        eventos.append("Taller")

    if poncharse(staLLanta)==True:
        eventos.append("Ponchado")
        if "Desponchadora" in eventos == False:
            continua = False

    if bateria(precipitaciones, tempMotor)==True:
        eventos.append("Fallo de bateria")
        if "Taller" in eventos == False:
            continua = False

    if calentamientoMotor(tempMotor, aceite, status)==True:
        eventos.append("Sobrecalentamiento del motor")
        N_aceite -= 12

    if aguaMotor(precipitaciones, neblina)==True:
        eventos.append("Agua en el motor")

    if animales(longitud, tipo, precipitaciones)==True:
        eventos.append("Choque con animal")
        if "Taller" in eventos == False:
            continua = False

    if choque(complejidad, status, precipitaciones, viento, neblina, velocidad, staLLanta, batalla)==True:
        eventos.append("Choque")
        if "Taller" in eventos == False:
            continua = False

    if lluvia(precipitaciones, viento)==True:
        eventos.append("Lluvias torrenciales")
        N_velocidad -= 10
        N_tempMotor -= 2

    if tormenta(precipitaciones, viento)==True:
        eventos.append("Tormenta electrica")
        N_velocidad -= 15
        N_staLLanta -= 9
    
    if rayo(batalla)==True:
        eventos.append("Impacto de rayo")
        if "Taller" in eventos == False:
            continua = False
    
    if visibilidad(neblina)==True:
        eventos.append("Perdida de visibilidad")
        N_velocidad -= 7

    if fantasmas(neblina, 30)==True:
        eventos.append("Fantasma")
        treas = True

    if tesoro(treas)==True:
        eventos.append("Tesoro")
        N_dinero += 4000

    if aventon(neblina, precipitaciones)==True:
        eventos.append("Aventon")
        N_dinero += 500

    if trafico(complejidad, status)==True:
        eventos.append("Trafico")
        N_velocidad -= 10
        N_gasCantidad -= 8

    if ave(viento, dirViento)==True:
        eventos.append("Ave en el parabrisas")
        N_velocidad -= 5

    if elevacion(peso, cilindraje)==True:
        eventos.append("Varado por peso")
        N_gasCantidad -= 12
        N_velocidad -= 12
        N_tempMotor += 5

    return [Carro2(N_velocidad, calidad, staCarro, tipoLLanta, N_staLLanta, N_gasCantidad, cilindraje, peso, aerodinamica, aceite, N_tempMotor, batalla, N_dinero)]
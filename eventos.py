import random
from funciones import promedio
from nodos import Carro

def gasolinera(complejidad):
    ra = random.randrange(1, 100)
    if(ra<complejidad):
        return "gasolinera"
    else:
        return "no"

def reten(velocidad, calidad, complejidad, dinero):
    ra = random.randrange(1, 100)
    cof = 20 
    resul = promedio(cof, velocidad) + promedio(cof, complejidad)
    if(ra<resul):
        return "reten"
    else:
        return "no"

def poncharse(status):
    ra = random.randrange(1, 100)
    if(ra<status/4):
        return "poncharse"
    else:
        return "no"

def desponchadora(tipo):
    ra = random.randrange(1, 100)
    if ra < tipo:
        return "desponchadora"
    else:
        return "no"

def bateria(precipitaciones, tempMotor):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, tempMotor)
    resul = cof/2
    if ra < resul:
        return "bateria"
    else:
        return "no"

def calentamientoMotor(tempMotor, aceite, status):
    ra = random.randrange(1, 100)
    cof = promedio(100, tempMotor) + promedio(100, aceite) + promedio(100, status)
    resul = cof / 3
    if ra < resul:
        return "Sobrecalentamiento"
    else:
        return "no"

def aguaMotor(precipitaciones, neblina):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, neblina)
    resul = cof / 2
    if ra < resul:
        return "Agua en el motor"
    else:
        return "no"

def taller(complejidad):
    ra = random.randrange(1, 100)
    if ra < complejidad:
        return "gasolinera"
    else:
        return "no"

def animales(longitud, tipo, precipitaciones):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, longitud)
    resul = cof / 2
    if ra < resul:
        return "Choque con animal"
    else:
        return "no"

def choque(complejidad, status, precipitaciones, viento, neblina, velocidad, stallanta, batalla):
    ra = random.randrange(1, 100)
    cof = promedio(100, complejidad) + promedio(100, status) + promedio(100, precipitaciones) + promedio(100, viento) + promedio(100, neblina) + promedio(100, stallanta) + promedio(100, batalla)
    resul = cof / 12
    if ra < resul:
        return "Choque"
    else:
        return "no"

def lluvia(precipitaciones, viento):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, viento)
    resul = cof / 2
    if ra < resul:
        return "Lluvias torrenciales"
    else:
        return "no"

def tormenta(precipitaciones, viento):
    ra = random.randrange(1, 100)
    cof = promedio(100, precipitaciones) + promedio(100, viento)
    resul = cof /1.3
    if ra < resul:
        return "Tormenta electrica"
    else:
        return "no"

def rayo(batalla):
    ra = random.randrange(1, 5)
    resul = batalla
    if ra > resul:
        return "Lluvias torrenciales"
    else:
        return "no"

def visibilidad(neblina):
    ra = random.randrange(1, 5)
    resul = neblina
    if ra > resul:
        return "Poca visibilidad"
    else:
        return "no"

def fantasmas(neblina, compania):
    ra = random.randrange(1, 5)
    resul = neblina + compania
    if ra > resul:
        return "Fantasmas"
    else:
        return "no"

def tesoro(trigger):
    ra = random.randrange(1, 50)
    comp = 100
    if trigger == True:
        comp = 50
    if ra < comp:
        return "Tesoro"
    else:
        return "no"

def aventon(neblina, precipitaciones):
    ra = random.randrange(1, 50)
    cof = promedio(100, neblina) + promedio(100, precipitaciones)
    resul = cof / 3
    if ra < resul:
        return "Aventon"
    else:
        return "no"

def trafico(complejidad, status):
    ra = random.randrange(1, 50)
    cof = promedio(100, complejidad) + promedio(100, status)
    resul = cof / 3
    if ra < resul:
        return "trafico"
    else:
        return "no"

def ave(viento, dirviento):
    ra = random.randrange(1, 50)
    if dirviento:
        ra=ra*0.2
    cof = viento*2
    if ra < cof:
        return "ave"
    else:
        return "no"

def elevacion(peso, cilindraje):
    ra = random.randrange(1, 50)

    resul = promedio(100, peso) / cilindraje
    if ra < resul:
        return "Elevacion"
    else:
        return "no"

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


    if gasolinera(complejidad)!="no":
        eventos.append("Gasolinera")
        if gasCantidad<=10:
            N_gasCantidad = 100
    
    if reten(velocidad, calidad, complejidad, dinero)!="no":
        eventos.append("Reten")
        if dinero<=0:
            continua = False
        elif calidad>70:
            N_dinero-=30
        else:
            N_dinero-=5

    if desponchadora(tipo)!="no":
        eventos.append("Desponchadora")

    if taller(complejidad)!="no":
        eventos.append("Taller")

    if poncharse(staLLanta)!="no":
        eventos.append("Ponchado")
        if "Desponchadora" in eventos == False:
            continua = False

    if bateria(precipitaciones, tempMotor)!="no":
        eventos.append("Fallo de bateria")
        if "Taller" in eventos == False:
            continua = False

    if calentamientoMotor(tempMotor, aceite, status)!="no":
        eventos.append("Sobrecalentamiento del motor")
        N_aceite -= 12

    if aguaMotor(precipitaciones, neblina)!="no":
        eventos.append("Agua en el motor")

    if animales(longitud, tipo, precipitaciones)!="no":
        eventos.append("Choque con animal")
        if "Taller" in eventos == False:
            continua = False

    if choque(complejidad, status, precipitaciones, viento, neblina, velocidad, staLLanta, batalla)!="no":
        eventos.append("Choque")
        if "Taller" in eventos == False:
            continua = False

    if lluvia(precipitaciones, viento)!="no":
        eventos.append("Lluvias torrenciales")
        N_velocidad -= 10
        N_tempMotor -= 2

    if tormenta(precipitaciones, viento)!="no":
        eventos.append("Tormenta electrica")
        N_velocidad -= 15
        N_staLLanta -= 9
    
    if rayo(batalla)!="no":
        eventos.append("Impacto de rayo")
        if "Taller" in eventos == False:
            continua = False
    
    if visibilidad(neblina)!="no":
        eventos.append("Perdida de visibilidad")
        N_velocidad -= 7

    if fantasmas(neblina, 30)!="no":
        eventos.append("Fantasma")
        treas = True

    if tesoro(treas)!="no":
        eventos.append("Tesoro")
        N_dinero += 4000

    if aventon(neblina, precipitaciones)!="no":
        eventos.append("Aventon")
        N_dinero += 500

    if trafico(complejidad, status):
        eventos.append("Trafico")
        N_velocidad -= 10
        N_gasCantidad -= 8

    if ave(viento, dirViento)!="no":
        eventos.append("Ave en el parabrisas")
        N_velocidad -= 5

    if elevacion(peso, cilindraje):
        eventos.append("Varado por peso")
        N_gasCantidad -= 12
        N_velocidad -= 12
        N_tempMotor += 5

    return [eventos, continua, Carro(N_velocidad, calidad, staCarro, tipoLLanta, N_staLLanta, N_gasCantidad, cilindraje, peso, aerodinamica, aceite, N_tempMotor, batalla, N_dinero)]
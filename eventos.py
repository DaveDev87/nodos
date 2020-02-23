import random
from funciones import promedio

def gasolinera(complejidad):
    ra = random.randrange(1, 100)
    if(ra<complejidad):
        return "gasolinera"
    else:
        return "no"

def reten(velocidad, calidad, complejidad):
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
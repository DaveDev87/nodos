from inspect import signature
import random

def tiempo(tiempo):
    resul = tiempo / 3600 * 100
    return int(resul)
    
def longitud(longitud):
    resul = longitud / 90000 * 100
    return int(resul)

def velocidad(velocidad):
    resul = (velocidad * (5/18)) / 30.55556 * 100
    return resul

def peso(peso):
    resul = peso / 2000 * 100
    return resul

def batalla(batalla):
    resul = batalla / 4.5 * 100
    return resul

def gasolina(gas):
    resul = gas / 65 * 100
    return resul

# MODIFICAR PROPIEDADES DEL CARRO

def promedio(a, b):
    return (a+b) / 2

def desfase(a):
    resul = 100 - a
    return resul



def changeVelocidad(vel, comple, tipo, caminoSta, tipoLLanta, llantaSta, peso, aero, batalla, longitud, precipitaciones, viento, dirviento, neblina):
    if dirviento:
        viento*=1
    else:
        viento*=-1
    resul = (promedio(vel, comple) + promedio(vel, tipo) + promedio(vel, caminoSta) + promedio(vel, llantaSta)
    + promedio(vel, peso) + promedio(vel, batalla) + promedio(vel, precipitaciones) + promedio(vel, viento) + 
    promedio(vel, neblina)) / (len(signature(changeVelocidad).parameters) - 4)
    return resul

    

def changeStaLLanta(llanta, tipo, status, longitud, precipitaciones):
    if tipo > 50:
        tip = 1500
    else:
        tip = 1000
    coeficiente = (desfase(status) + desfase(precipitaciones)) / tip
    resul = llanta - (coeficiente*longitud)
    return resul

def changeGas(gas, longitud, cilindros):

    coeficiente = (100 - (100 / cilindros)) / 1000
    resul = gas - (coeficiente * longitud)
    return resul

def changeAceite(aceite, longitud, temp):
    coeficiente = temp - 90
    border = coeficiente / 10
    if coeficiente > 0:
        resul = (aceite - border) 
    else:
        resul = aceite
    return resul



# PROBABILIDADES DE QUE OCURRAN LOS EVENTOS

def gasolinera(complejidad):
    ra = random.randrange(1, 100)
    if(ra<complejidad):
        return True
    else:
        return False

def reten(velocidad, calidad, complejidad):
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
    if(ra<tipo):
        return True
    else:
        return False
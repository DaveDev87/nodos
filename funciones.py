from inspect import signature

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
    return (a+b)/2



def changeVelocidad(vel, comple, tipo, caminoSta, tipoLLanta, llantaSta, peso, aero, batalla, longitud, precipitaciones, viento, dirviento, neblina):
    if dirviento:
        viento*=1
    else:
        viento*=-1
    resul = (promedio(vel, comple) + promedio(vel, tipo) + promedio(vel, caminoSta) + promedio(vel, llantaSta)
    + promedio(vel, peso) + promedio(vel, batalla) + promedio(vel, precipitaciones) + promedio(vel, viento) + 
    promedio(vel, neblina)) / (len(signature(changeVelocidad).parameters) - 4)
    return resul

    

def changeStaLLanta(llanta, tipo, status, longitud):
    return llanta

def changeGas(gas, longitud, cilindros):
    
    if cilindros == 4:
        resultado = 0.075 * longitud
    elif cilindros == 6:
        res = 0.075 * longitud
        resultado = res * 1.05
    elif cilindros==8:
        res = 0.075 * longitud
        resultado = res * 1.08


    final = gas - resultado
    return final


# PROBABILIDADES DE QUE OCURRAN LOS EVENTOS


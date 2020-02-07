
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

def changeVelocidad(vel, comple, tipo, caminoSta, tipoLLanta, llantaSta, peso, aero, batalla, longitud):
    velocidad = vel
    if longitud > 0:
        if tipo > 50:
            if tipoLLanta > 50:
                velocidad *= 0.92
            else:
                velocidad *= 0.95
        elif tipo < 75:
            if tipoLLanta > 50:
                velocidad
            else:
                velocidad *= 0.97

        if comple < 80:
            velocidad *= 0.95
            if tipoLLanta > 50:
                velocidad *= 0.96
            elif tipoLLanta < 75:
                velocidad *= 0.98
            if peso > 75:
                velocidad *=0.95
            if llantaSta < 51:
                velocidad *= 0.95

        if aero < 80:
            velocidad *= 0.95
        if caminoSta < 75:
            velocidad *= 0.94
            
    return velocidad

def changeStaLLanta(llanta, tipo, status, longitud):
    cont = 0

    if tipo > 50:
        cont = 0.00095
    
    cont += float("0.0000"+str(status))
    

    sub = cont * longitud
    final = llanta - sub
    return final

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


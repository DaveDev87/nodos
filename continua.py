from promedios import promedios as datos

def decision(complejidad, calidad, velocidad, dinero, tipo, staLLanta, precipitaciones, tempMotor, aceite, status, neblina, longitud, statusCar, viento, batalla, peso, cilindraje):
    refuerzo = 0
    rango = 3
    
    if complejidad<datos["gasolinera"]["complejidad"]+rango and complejidad>datos["gasolinera"]["complejidad"]-rango:
        refuerzo+=datos["gasolinera"]["ref"]

    if (complejidad<datos["reten"]["complejidad"]+rango and complejidad>datos["reten"]["complejidad"]-rango) + (calidad<datos["reten"]["complejidad"]+rango and calidad>datos["reten"]["complejidad"]-rango) + (velocidad<datos["reten"]["velocidad"]+rango and velocidad>datos["reten"]["velocidad"]-rango):
        refuerzo+=datos["reten"]["ref"]

    if tipo<datos["desponchadora"]["tipo"]+rango and tipo>datos["desponchadora"]["tipo"]-rango:
        refuerzo+=datos["desponchadora"]["ref"]

    if complejidad<datos["taller"]["complejidad"]+rango and complejidad>datos["taller"]["complejidad"]-rango:
        refuerzo+=datos["taller"]["ref"]

    if staLLanta<datos["poncharse"]["staLLanta"]+rango and staLLanta>datos["poncharse"]["staLLanta"]-rango:
        refuerzo+=datos["poncharse"]["ref"]

    if (precipitaciones<datos["bateria"]["precipitaciones"]+rango and precipitaciones>datos["bateria"]["precipitaciones"]-rango) and (tempMotor<datos["bateria"]["tempMotor"]+rango and tempMotor>datos["bateria"]["tempMotor"]-rango):
        refuerzo+=datos["bateria"]["ref"]

    if (tempMotor<datos["sobrecalentamiento"]["tempMotor"]+rango and tempMotor>datos["sobrecalentamiento"]["tempMotor"]-rango) + (aceite<datos["sobrecalentamiento"]["aceite"]+rango and aceite>datos["sobrecalentamiento"]["aceite"]-rango) + (status<datos["sobrecalentamiento"]["status"]+rango and status>datos["sobrecalentamiento"]["status"]-rango):
        refuerzo+=datos["sobrecalentamiento"]["ref"]

    if (precipitaciones<datos["aguaMotor"]["precipitaciones"]+rango and precipitaciones>datos["aguaMotor"]["precipitaciones"]-rango) and (neblina<datos["aguaMotor"]["neblina"]+rango and neblina>datos["aguaMotor"]["neblina"]-rango):
        refuerzo+=datos["aguaMotor"]["ref"]

    if (longitud<datos["animales"]["longitud"]+rango and longitud>datos["animales"]["longitud"]-rango) and (tipo<datos["animales"]["tipo"]+rango and tipo>datos["animales"]["tipo"]-rango) + (precipitaciones<datos["animales"]["precipitaciones"]+rango and precipitaciones>datos["animales"]["precipitaciones"]-rango):
        refuerzo+=datos["animales"]["ref"]

    if (complejidad<datos["choque"]["complejidad"]+rango and complejidad>datos["choque"]["complejidad"]-rango) and (statusCar<datos["choque"]["statusCar"]+rango and statusCar>datos["choque"]["statusCar"]-rango) + (precipitaciones<datos["choque"]["precipitaciones"]+rango and precipitaciones>datos["choque"]["precipitaciones"]-rango) + (viento<datos["choque"]["viento"]+rango and viento>datos["choque"]["viento"]-rango) + (neblina<datos["choque"]["neblina"]+rango and neblina>datos["choque"]["neblina"]-rango) + (velocidad<datos["choque"]["velocidad"]+rango and velocidad>datos["choque"]["velocidad"]-rango) + (status<datos["choque"]["status"]+rango and status>datos["choque"]["status"]-rango) + (batalla<datos["choque"]["batalla"]+rango and batalla>datos["choque"]["batalla"]-rango):
        refuerzo+=datos["choque"]["ref"]

    if (precipitaciones<datos["lluvia"]["precipitaciones"]+rango and precipitaciones>datos["lluvia"]["precipitaciones"]-rango) and (viento<datos["lluvia"]["viento"]+rango and viento>datos["lluvia"]["viento"]-rango):
        refuerzo+=datos["lluvia"]["ref"]

    if (precipitaciones<datos["tormenta"]["precipitaciones"]+rango and precipitaciones>datos["tormenta"]["precipitaciones"]-rango) and (viento<datos["tormenta"]["viento"]+rango and viento>datos["tormenta"]["viento"]-rango):
        refuerzo+=datos["tormenta"]["ref"]

    if batalla<datos["rayo"]["batalla"]+rango and batalla>datos["rayo"]["batalla"]-rango:
        refuerzo+=datos["rayo"]["ref"]

    if neblina<datos["visibilidad"]["neblina"]+rango and neblina>datos["visibilidad"]["neblina"]-rango:
        refuerzo+=datos["visibilidad"]["ref"]

    if neblina<datos["fantasmas"]["neblina"]+rango and neblina>datos["fantasmas"]["neblina"]-rango:
        refuerzo+=datos["fantasmas"]["ref"]

    if dinero<datos["tesoro"]["dinero"]+rango and dinero>datos["tesoro"]["dinero"]-rango:
        refuerzo+=datos["tesoro"]["ref"]

    if (precipitaciones<datos["aventon"]["precipitaciones"]+rango and precipitaciones>datos["aventon"]["precipitaciones"]-rango) and (neblina<datos["aventon"]["neblina"]+rango and neblina>datos["aventon"]["neblina"]-rango):
        refuerzo+=datos["aventon"]["ref"]

    if (complejidad<datos["trafico"]["complejidad"]+rango and complejidad>datos["trafico"]["complejidad"]-rango) and (status<datos["trafico"]["status"]+rango and status>datos["trafico"]["status"]-rango):
        refuerzo+=datos["trafico"]["ref"]

    if viento<datos["ave"]["viento"]+rango and viento>datos["ave"]["viento"]-rango:
        refuerzo+=datos["ave"]["ref"]

    if peso<datos["elevacion"]["peso"]+rango and peso>datos["elevacion"]["peso"]-rango:
        refuerzo+=datos["elevacion"]["ref"]


    if refuerzo>=-2:
        return True
    else:
        return False

# print(decision(55,10,10,10,10,50,10,10,10,10,10,10,10,10,10,10,8))



# print(datos["gasolinera"]["complejidad"])

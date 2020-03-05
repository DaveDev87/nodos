import json
from statistics import mean

content = ""

promedios = {
    "gasolinera": {
        "complejidad": [],
        "ref": 1
    },
    "reten":{ 
        "complejidad": [],
        "calidad": [],
        "velocidad": [],
        "dinero": [],
        "ref": -1
    },
    "desponchadora": {
        "tipo": [],
        "ref": 1
    },
    "taller": {
        "complejidad": [],
        "ref": 1
    },
    "poncharse": {
        "staLLanta": [],
        "ref": -1
    },
    "bateria": {
        "precipitaciones": [],
        "tempMotor": [],
        "ref": -1
    },
    "sobrecalentamiento":{
        "tempMotor": [],
        "aceite": [],
        "status": [],
        "ref": -1
    },
    "aguaMotor":{
        "precipitaciones": [],
        "neblina": [],
        "ref": -1
    },
    "animales": {
        "longitud": [],
        "tipo": [],
        "precipitaciones": [],
        "ref": -1
    },
    "choque": {
        "complejidad": [],
        "statusCar": [],
        "precipitaciones": [],
        "viento": [],
        "neblina": [],
        "velocidad": [],
        "status": [],
        "batalla": [],
        "ref": -1
    },
    "lluvia":{
        "precipitaciones": [],
        "viento": [],
        "ref": -1
    },
    "tormenta": {
        "precipitaciones": [],
        "viento": [],
        "refuerzo": -1
    },
    "rayo":{
        "batalla": [0],
        "ref": -1
    },
    "visibilidad":{
        "neblina": [0],
        "ref": -1
    },
    "fantasmas":{
        "neblina": [0],
        "ref": -1
    },
    "tesoro":{
        "dinero": [],
        "refuerzo": 1
    },
    "aventon":{
        "precipitaciones": [],
        "neblina": [],
        "ref": 1
    },
    "trafico":{
        "complejidad": [],
        "status": [],
        "ref": -1
    },
    "ave":{
        "viento": [],
        "dirviento": True,
        "ref": -1
    },
    "elevacion":{
        "peso": [],
        "cilindraje": [],
        "ref": -1
    }
}


with open("data.txt", "r") as f:
    content = f.read()
content = json.loads(content)


for item in content:
    # gas = list(filter(lambda x: x["evento"]=="gasolinera" and x["triggered"]==True, item))
    if item[0]["triggered"]==True:
        promedios["gasolinera"]["complejidad"].append(item[0]["complejidad"])

    if item[1]["triggered"]==True:
        promedios["reten"]["complejidad"].append(item[1]["complejidad"])
        promedios["reten"]["calidad"].append(item[1]["calidad"])
        promedios["reten"]["velocidad"].append(item[1]["velocidad"])
        promedios["reten"]["dinero"].append(item[1]["dinero"])

    if item[2]["triggered"]==True:
        promedios["desponchadora"]["tipo"].append(item[2]["tipo"])

    if item[3]["triggered"]==True:
        promedios["taller"]["complejidad"].append(item[3]["complejidad"])

    if item[4]["triggered"]==True:
        promedios["poncharse"]["staLLanta"].append(item[4]["staLLanta"])

    if item[5]["triggered"]==True:
        promedios["bateria"]["precipitaciones"].append(item[5]["precipitaciones"])
        promedios["bateria"]["tempMotor"].append(item[5]["tempMotor"])

    if item[6]["triggered"]==True:
        promedios["sobrecalentamiento"]["tempMotor"].append(item[6]["tempMotor"])
        promedios["sobrecalentamiento"]["aceite"].append(item[6]["aceite"])
        promedios["sobrecalentamiento"]["status"].append(item[6]["status"])

    if item[7]["triggered"]==True:
        promedios["aguaMotor"]["precipitaciones"].append(item[7]["precipitaciones"])
        promedios["aguaMotor"]["neblina"].append(item[7]["neblina"])

    if item[8]["triggered"]==True:
        promedios["animales"]["longitud"].append(item[8]["longitud"])
        promedios["animales"]["tipo"].append(item[8]["tipo"])
        promedios["animales"]["precipitaciones"].append(item[8]["precipitaciones"])

    if item[9]["triggered"]==True:
        promedios["choque"]["complejidad"].append(item[9]["complejidad"])
        promedios["choque"]["statusCar"].append(item[9]["statusCar"])
        promedios["choque"]["precipitaciones"].append(item[9]["precipitaciones"])
        promedios["choque"]["viento"].append(item[9]["viento"])
        promedios["choque"]["neblina"].append(item[9]["neblina"])
        promedios["choque"]["velocidad"].append(item[9]["velocidad"])
        promedios["choque"]["status"].append(item[9]["status"])
        promedios["choque"]["batalla"].append(item[9]["batalla"])

    if item[10]["triggered"]==True:
        promedios["lluvia"]["precipitaciones"].append(item[10]["precipitaciones"])
        promedios["lluvia"]["viento"].append(item[10]["viento"])

    if item[11]["triggered"]==True:
        promedios["tormenta"]["precipitaciones"].append(item[11]["precipitaciones"])
        promedios["tormenta"]["viento"].append(item[11]["viento"])

    if item[12]["triggered"]==True:
        promedios["rayo"]["batalla"].append(item[12]["batalla"])

    if item[13]["triggered"]==True:
        promedios["visibilidad"]["neblina"].append(item[13]["neblina"])

    if item[14]["triggered"]==True:
        promedios["fantasmas"]["neblina"].append(item[15]["neblina"])

    if item[15]["triggered"]==True:
        promedios["tesoro"]["dinero"].append(item[15]["dinero"])

    if item[16]["triggered"]==True:
        promedios["aventon"]["precipitaciones"].append(item[16]["precipitaciones"])
        promedios["aventon"]["neblina"].append(item[16]["neblina"])

    if item[17]["triggered"]==True:
        promedios["trafico"]["complejidad"].append(item[17]["complejidad"])
        promedios["trafico"]["status"].append(item[17]["status"])

    if item[18]["triggered"]==True:
        promedios["ave"]["viento"].append(item[18]["viento"])

    if item[19]["triggered"]==True:
        promedios["elevacion"]["peso"].append(item[19]["peso"])
        promedios["elevacion"]["cilindraje"].append(item[19]["cilindraje"])


# print(json.dumps(gasList, indent=4))
promedios["gasolinera"]["complejidad"]=int(mean(promedios["gasolinera"]["complejidad"]))

promedios["reten"]["complejidad"]=int(mean(promedios["reten"]["complejidad"]))
promedios["reten"]["calidad"]=int(mean(promedios["reten"]["calidad"]))
promedios["reten"]["velocidad"]=int(mean(promedios["reten"]["velocidad"]))
promedios["reten"]["dinero"]=int(mean(promedios["reten"]["dinero"]))

promedios["desponchadora"]["tipo"]=int(mean(promedios["desponchadora"]["tipo"]))

promedios["taller"]["complejidad"]=int(mean(promedios["taller"]["complejidad"]))

promedios["poncharse"]["staLLanta"]=int(mean(promedios["poncharse"]["staLLanta"]))

promedios["bateria"]["precipitaciones"]=int(mean(promedios["bateria"]["precipitaciones"]))
promedios["bateria"]["tempMotor"]=int(mean(promedios["bateria"]["tempMotor"]))

promedios["sobrecalentamiento"]["tempMotor"]=int(mean(promedios["sobrecalentamiento"]["tempMotor"]))
promedios["sobrecalentamiento"]["aceite"]=int(mean(promedios["sobrecalentamiento"]["aceite"]))
promedios["sobrecalentamiento"]["status"]=int(mean(promedios["sobrecalentamiento"]["status"]))

promedios["aguaMotor"]["precipitaciones"]=int(mean(promedios["aguaMotor"]["precipitaciones"]))
promedios["aguaMotor"]["neblina"]=int(mean(promedios["aguaMotor"]["neblina"]))

promedios["animales"]["longitud"]=int(mean(promedios["animales"]["longitud"]))
promedios["animales"]["tipo"]=int(mean(promedios["animales"]["tipo"]))
promedios["animales"]["precipitaciones"]=int(mean(promedios["animales"]["precipitaciones"]))

promedios["choque"]["complejidad"]=int(mean(promedios["choque"]["complejidad"]))
promedios["choque"]["statusCar"]=int(mean(promedios["choque"]["statusCar"]))
promedios["choque"]["precipitaciones"]=int(mean(promedios["choque"]["precipitaciones"]))
promedios["choque"]["viento"]=int(mean(promedios["choque"]["viento"]))
promedios["choque"]["neblina"]=int(mean(promedios["choque"]["neblina"]))
promedios["choque"]["velocidad"]=int(mean(promedios["choque"]["velocidad"]))
promedios["choque"]["status"]=int(mean(promedios["choque"]["status"]))
promedios["choque"]["batalla"]=int(mean(promedios["choque"]["batalla"]))

promedios["lluvia"]["precipitaciones"]=int(mean(promedios["lluvia"]["precipitaciones"]))
promedios["lluvia"]["viento"]=int(mean(promedios["lluvia"]["viento"]))

promedios["tormenta"]["precipitaciones"]=int(mean(promedios["tormenta"]["precipitaciones"]))
promedios["tormenta"]["viento"]=int(mean(promedios["tormenta"]["viento"]))

promedios["rayo"]["batalla"]=int(mean(promedios["rayo"]["batalla"]))

promedios["visibilidad"]["neblina"]=int(mean(promedios["visibilidad"]["neblina"]))

promedios["fantasmas"]["neblina"]=int(mean(promedios["fantasmas"]["neblina"]))

promedios["tesoro"]["dinero"]=int(mean(promedios["tesoro"]["dinero"]))

promedios["aventon"]["precipitaciones"]=int(mean(promedios["aventon"]["precipitaciones"]))
promedios["aventon"]["neblina"]=int(mean(promedios["aventon"]["neblina"]))

promedios["trafico"]["complejidad"]=int(mean(promedios["trafico"]["complejidad"]))
promedios["trafico"]["status"]=int(mean(promedios["trafico"]["status"]))

promedios["ave"]["viento"]=int(mean(promedios["ave"]["viento"]))

promedios["elevacion"]["peso"]=int(mean(promedios["elevacion"]["peso"]))
promedios["elevacion"]["cilindraje"]=int(mean(promedios["elevacion"]["cilindraje"]))


# print(json.dumps(promedios, indent=4))

# print(promedios["gasolinera"]["complejidad"])

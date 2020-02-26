import json

class Persona:
    def __init__(self):
        self.simon = True
        self.nelson = False
        self.datass = [
            {"hola": 9900},
            {"prueba": 3000}
        ]

a = Persona()
b = [a.__dict__]
filterList = list(filter(lambda x: x["nelson"]==False, b))
print(filterList)

with open("data.json", "w",encoding="utf-8") as f:
    json.dump(b, f, ensure_ascii=False, indent=4)

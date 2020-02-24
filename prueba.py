import json

class Persona:
    def __init__(self):
        self.simon = True
        self.nelson = False

a = Persona()
b = [a.__dict__, a.__dict__]
print(b)

with open("data.txt", "w",encoding="utf-8") as f:
    json.dump(b, f, ensure_ascii=False, indent=4)

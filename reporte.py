import pandas as pd
from nodos import caminos as datos

comple = []
tiem = []
tip = []
sta = []
lon = []

for item in datos[0]:
    comple.append(item.complejidad)
    tiem.append(item.tiempo)
    tip.append(item.tipo)
    sta.append(item.status)
    lon.append(item.longitud)

df = pd.DataFrame({"Complejidad": comple,
                    "Tiempo": tiem,
                    "Tipo": tip,
                    "status": sta,
                    "Longitud": lon})

writer = pd.ExcelWriter("demo.xlsx", engine="xlsxwriter")

df.to_excel(writer, sheet_name="Prueba", index=False)

writer.save()
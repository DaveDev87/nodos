import pandas as pd
from nodos import caminos as datos
from nodos import carroLista as car

comple = []
tiem = []
tip = []
sta = []
lon = []
pre = []
vien = []
dirvien = []

vel = []

for item in car:
    vel.append(int(item.velocidad))

for item in datos[0]:
    comple.append(item.complejidad)
    tiem.append(item.tiempo)
    tip.append(item.tipo)
    sta.append(item.status)
    lon.append(item.longitud)
    pre.append(item.precipitaciones)
    vien.append(item.viento)
    if item.dirViento == True:
        dirvien.append("A favor")
    else:
        dirvien.append("En contra")

df = pd.DataFrame({"Complejidad": comple,
                    "Tiempo": tiem,
                    "Tipo": tip,
                    "status": sta,
                    "Longitud": lon,
                    "Precipitaciones": pre,
                    "Viento": vien,
                    "Dirección": dirvien,
                    "velocidad": vel
                    })

writer = pd.ExcelWriter("demo.xlsx", engine="xlsxwriter")

df.to_excel(writer, sheet_name="Prueba", index=False)

writer.save()
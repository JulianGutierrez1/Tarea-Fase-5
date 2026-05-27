# Julian David Gutierrez Salinas  
# 850
# Ingenieria de sistemas
# Codigo fuente: autoria propia
equipo = [
    ["Juan",     8, 9, 8, 10, 7],
    ["Carlos",   7, 7, 8,  8, 8],
    ["Maria",  9, 9, 9,  9, 9],
    ["Julian ",    6, 7, 6,  7, 5],
]

JornadaHoras = 40

def calcular_jornada(fila):
    nombre = fila[0]
    horas_dias = fila[1:]
    
    total = 0
    for h in horas_dias:
        total = total + h
    
    if total > JornadaHoras:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estandar"
    return nombre, total, clasificacion

print("===========================================================================")
print("|         MATRIZ DE HORAS SEMANALES DEL EQUIPO                            |")
print("===========================================================================")
print("")

print("===============================================================================================")
print("| No | Nombre         | Lunes | Mart. | Mierc.   | Juev. | Viern. | Total | Jornada         |")
print("===============================================================================================")

numero = 1
resultados = []

for fila in equipo:
    nombre, total, clasificacion = calcular_jornada(fila)
    print(f"| {numero}  | {nombre:<14} |   {fila[1]}   |   {fila[2]}   |    {fila[3]}     |   {fila[4]}   |    {fila[5]}   |   {total}  | {clasificacion:<15} |")
    print("-----------------------------------------------------------------------------------------------")
    numero = numero + 1
    resultados.append((nombre, total, clasificacion))
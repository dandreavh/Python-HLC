diccionario = {
    'emp1': {'nombre': 'Plantinancio', 'salario': 7500},
    'emp2': {'nombre': 'Herbijuan', 'salario': 8000},
    'emp3': {'nombre': 'Ovinante', 'salario': 6500}
    }
for empleado in diccionario.values():
    if empleado["nombre"] == "Ovinante":
        empleado["salario"] = 8500
print(diccionario)
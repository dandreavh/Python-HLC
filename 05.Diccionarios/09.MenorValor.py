diccionario = {
        'Física': 82,
        'Matemáticas': 65,
        'Historia': 75
    }
minimo = min(diccionario.values())
for key, value in diccionario.items():
    if minimo == value:
        print(key)
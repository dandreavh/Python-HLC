diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }

keysToRemove = ["nombre", "salario"]
del diccionario[keysToRemove[0]]
del diccionario[keysToRemove[1]]
print(diccionario)
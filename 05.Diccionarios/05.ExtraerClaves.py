diccionario = {
    "nombre": "Pikolo",
    "edad":28,
    "salario": 8000,
    "planeta": "Namek"
    }

#Claves para extraer:
keys = ["nombre", "salario"]
new_dict = {keys[0]:diccionario[keys[0]], keys[1]:diccionario[keys[1]]}
print(new_dict)
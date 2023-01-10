print("Hola mundo :)")
# comentarios
nombre = input("Introduce tu nombre por pantalla:")
print("Hola,", nombre, "eres buena gente")

# print imprime por pantalla
# print + end indica qué hay después sin salto de línea print("Sevilla", end=" ") --> 

i = "3"
print(f"variable {i}")

# una tupla es una lista de solo lectura
tupla = ("hola", 3)
listas = [1, "hola"]
diccionario = {"uno":1, "dos":2}

nota = int(print("Indica la nota"))
if nota < 5:
    print("Suspenso")
else:
    print("Aprobado")

if 0 < nota < 5:
    print("suspenso")

# in --> para saber si está en una lista o tupla
# and --> comparador y or 
# Acepte tres cadenas cualquiera de una llamada input(). 
# Escriba un programa para tomar tres nombres como entrada de un usuario con una única llamada 
# a función input().
i = 1
lista = []
while i < 4:
    nombre = input("Introduzca un nombre: ")
    lista.append(nombre)
    i += 1
print(lista)

nombre1, nombre2, nombre3 = input("Introduzca 3 nombres").split()
print(nombre1)
print(nombre2)
print(nombre3)
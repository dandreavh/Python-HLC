# Dada una cadena de longitud impar mayor que 7, 
# devuelva una nueva cadena formada por los tres caracteres del medio de una cadena determinada
cadena = input("Introduzca una cadena de longitud impar mayor que 7: ")
while ((len(cadena) < 7) and (int(len(cadena)/2) == 0)):
    cadena = input("Introduzca una cadena de longitud impar mayor que 7: ")
    print(len(cadena))
newString = cadena[int(len(cadena)/2)-1] + cadena[int(len(cadena)/2)] + cadena[int(len(cadena)/2)+1]
print(newString)
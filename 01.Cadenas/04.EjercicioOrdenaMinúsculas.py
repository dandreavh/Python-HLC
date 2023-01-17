cadena = input("Introduzca una cadena con mayúsculas y minúsculas: ")
min = ""
may = ""
for letra in cadena:
    if(letra.islower()):
        min += letra
    else:
        may += letra
print(min+may)
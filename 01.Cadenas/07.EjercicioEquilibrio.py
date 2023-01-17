s1 = input("Introduzca una cadena: ")
s2 = input("Introduzca otra cadena: ")
esta = 0
noEsta = 0
for letra in s1:
    if letra in s2:
        esta+=1
    else: noEsta +=1
if(noEsta > 0):
    print("No están equilibradas las cadenas")
else: print("Las cadenas están equilibradas")
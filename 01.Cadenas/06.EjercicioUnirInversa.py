s1 = input("Introduzca una cadena: ")
s2 = input("Introduzca otra cadena: ")[::-1]
newString = ""
if(len(s1)<len(s2)):
    menor = s1
    mayor = s2
else:
    menor = s2
    mayor = s1
for i in range(len(menor)):
    newString += s1[i] + s2[i]
newString += mayor[len(menor):]
print(newString)

s1 = input("Introduzca una cadena: ")
s2 = input("Introduzca otra cadena: ")
s1_primeraMitad = s1[:int(len(s1)/2)]
s1_segundaMitad = s1[int(len(s1)/2):]
newString = s1_primeraMitad + s2 + s1_segundaMitad
print(newString)
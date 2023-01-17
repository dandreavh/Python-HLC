s1 = input("Introduzca una cadena: ")
s2 = input("Introduzca otra cadena: ")
newString = s1[0] + s2[0] + s1[int(len(s1)/2)] + s2[int(len(s2)/2)] + s1[int(len(s1)-1)] + s2[int(len(s2)-1)]
print(newString)
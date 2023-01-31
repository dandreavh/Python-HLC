lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]
aux = []
for i in range(len(lista1)):
    aux.append(lista1[i]+lista2[i])
result = ""
for word in aux:
    result += word +" "
print(result)
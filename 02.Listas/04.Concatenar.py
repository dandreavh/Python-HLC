lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]
result = []

for item1 in lista1:
    for item2 in lista2:
        union = item1 + item2
        result.append(union)
print(result)
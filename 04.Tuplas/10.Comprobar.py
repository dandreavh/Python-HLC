tupla = (45, 45, 45, 45)
primer_elemento = tupla[0]
iguales = True
for elemento in tupla:
    if elemento != primer_elemento:
        iguales = False
        break
print(iguales)
lista = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublista = ["h", "i", "j"]
for i in range(len(sublista)):
    lista[2][1][2].append(sublista[i])
print(lista)
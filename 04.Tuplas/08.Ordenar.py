tupla = (('a', 23),('b', 37),('c', 11), ('d',29))
lista_tupla = list(tupla)
lista_tupla.sort(key = lambda x:x[1])
print(lista_tupla)
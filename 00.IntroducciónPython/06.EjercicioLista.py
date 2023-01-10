# Acepte una lista de 5 números flotantes como entrada del usuario.
lista = []
i = 1
while i < 6:
    num = float(input("Introduzca un número decimal: "))
    lista.append(num)
    i += 1
print("Su lista:", lista)
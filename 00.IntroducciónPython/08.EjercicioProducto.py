# Calcula la multiplicación y la suma de dos números. Dados dos números enteros, 
# devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, devuelve su suma.
numero1 = int(input("Introduzca un número"))
numero2 = int(input("Introduzca otro número"))
suma = numero1 + numero2
multiplicacion = numero1 * numero2
if multiplicacion > 1000:
    print("El producto es ", multiplicacion)
else:
    print("El suma es ", suma)
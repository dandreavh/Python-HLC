str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
numbers = [int(fragmento)for fragmento in str1.split() if fragmento.isdigit()]
suma = 0
for num in numbers:
    suma = suma + num
promedio = suma / len(numbers)
print("La suma es",suma)
print("El promedio es",promedio)
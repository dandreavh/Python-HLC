numeros = [12, 75, 150, 180, 145, 525, 50]
# El número debe ser divisible por cinco. 
# Si el número es mayor que 150, omítalo y pasa al siguiente número. 
# Si el número es mayor que 500, detén el bucle
for num in numeros:
    if num % 5 == 0:
        if num > 150:
            continue
        if num > 500:
            break
        else:
            print(num)
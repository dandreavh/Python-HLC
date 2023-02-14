def suma(num):
    if num > 1:
        num = num + suma(num -1)
    return num
print(suma(10))
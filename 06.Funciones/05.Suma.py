""" Cree una función externa que acepte dos parámetros a y b
Cree una función interna dentro de una función externa que calculará la suma de a y b
Por último, una función externa agregará 5 y lo devolverá """

def calcular(a, b):
    def suma(a, b):
        return a + b
    return add5(suma(a, b))

def add5(suma):
    result = suma + 5
    return result

print(calcular(1,2))
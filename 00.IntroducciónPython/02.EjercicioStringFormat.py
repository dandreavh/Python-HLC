# Aplicar formato a las variables mediante el método string.format().
# Escriba un programa para usar el método string.format() 
# para formatear las siguientes tres variables según la salida esperada.
# Resultado: Tengo 1000 euros para comprar 3 tarjetas gráficas por 450,00 dólares.

resultado = "Tengo {totalMoney:} euros para comprar {quantity} tarjetas gráficas por {price:.2f} dólares."
print(resultado.format(totalMoney = 1000, quantity = 3, price = 450))
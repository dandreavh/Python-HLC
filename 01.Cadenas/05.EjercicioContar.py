cadena = input("Introduzca una cadena")
caracteres = 0
digitos = 0
simbolos = 0
for i in cadena:
    if(i.isdigit()):
        digitos+=1 # okk
    elif(i.isalpha()):
        caracteres+=1
    else:
        simbolos+=1
print("Recuentos totales: \n Caracteres = "+str(caracteres)+"\n Dígitos = "+str(digitos)+"\n Símboloes = "+str(simbolos))
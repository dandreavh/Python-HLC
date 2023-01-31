# Se puede plantear con el maketrans, translate y string.punctuation
str1 = "/*Chema es @profesor & maker"
result = ""
for element in str1:
    if element.isalnum() or element == " ":
        result = result + element
print(result)
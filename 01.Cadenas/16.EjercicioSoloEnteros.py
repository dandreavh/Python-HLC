str1 = "Tengo 39 años y 10 meses".split()
result = ""
for element in str1:
    if element.isnumeric():
        result = result + element
print(result)
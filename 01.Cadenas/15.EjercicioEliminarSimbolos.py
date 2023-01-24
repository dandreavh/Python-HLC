str1 = "/*Chema es @profesor &amp; maker"
result = ""
for element in str1:
    if element.isalnum() or element == " ":
        result = result + element
print(result)
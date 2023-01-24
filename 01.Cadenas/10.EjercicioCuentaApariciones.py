str1 = "Apple".lower()
result = {}
for letra in str1:
    if letra not in result.keys():
        result[letra] = 1
    else:
        result[letra] += 1
print(result)
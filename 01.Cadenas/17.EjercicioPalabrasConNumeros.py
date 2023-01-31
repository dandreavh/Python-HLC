str1 = "Chema39 es profesor10 y maker".split()
result = ""
for item in str1:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        result += item
print(result)
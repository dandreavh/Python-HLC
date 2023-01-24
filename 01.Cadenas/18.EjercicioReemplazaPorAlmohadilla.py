str1 = '/*!!Chema es!! @profesor & maker!!---'
# tengo que hacer una auxiliar para que no se pierda la modificación
new_str = ""
for chr in str1:
    if not(chr.isalpha()):
        print(chr)
        new_str = str1.replace(chr, "#")
    print(new_str)
print(new_str)

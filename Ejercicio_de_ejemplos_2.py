#Practica2
frace=(input("Introduce cualquiera frace ")).lower()
vocales="aeiou"
total_vocales=0
for i in frace:
    if i in vocales:
        total_vocales+=1
print(f"El número total de vocales de este frace és: {total_vocales}")


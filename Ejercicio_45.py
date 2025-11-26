#Programa45
palabra=input("Introduce una palabra: ")
vocales=""
consonantes=""
for i in palabra:
    if i in "aeiouáéíóúàèìòù":
        vocales+=i
    else:
        consonantes+=i
print(f"Las vocales de la palabra {palabra} són: {vocales}")
print(f"Las consonantes de la palabra {palabra} són: {consonantes}")


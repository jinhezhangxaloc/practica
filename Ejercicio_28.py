#Programa28
letra=input("Introduce una letra, un numero o un símbolo: ")
es_letra = ()
if letra.isalpha():
    es_letra = True
    if letra.isupper():
        mayuscula = True
        if mayuscula == True:
            print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
elif letra.isalnum():
    print("El valor introducido es un número")
else:
    print("El valor introducido es un símbolo")
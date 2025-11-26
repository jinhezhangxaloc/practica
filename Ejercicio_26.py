#Programa26
letra=input("Introduce una letra: ")
mayuscula = ()
if letra.isupper():
    mayuscula = True
    if mayuscula == True:
        print("La letra es mayúscula")
else:
    if letra.isdigit() :
        print("La letra es mayúscula ¿?")
    else:
        mayuscula = False
        print("La letra es minúscula")

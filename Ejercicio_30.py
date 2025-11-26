#Programa30
frase=input("Introduce una frase: ")
caracteres=len(frase)
if len(frase) == 11 :
    print("La frase tiene 11 caracteres")
elif len(frase) < 11 :
    print("La frase tiene menos de 11 caracteres")
elif len(frase) > 11 :
    print("La frase tiene 11 o más caracteres")
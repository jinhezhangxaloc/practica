#Programa43
posicion=0
palabra=input("Introduce una palabra ")
for i in range(len(palabra)):
    print(f"En la posición {posicion} está la {palabra[int(posicion)]}")
    posicion+=1


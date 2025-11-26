#Programa48
palabra=input("Introduce la palabra secreta: ")
for i in range(len(palabra)):
    letra=input("Introduce una letra: ")
    if letra in palabra:
        print("la letra existe")
    else:
        print("la letra no existe")



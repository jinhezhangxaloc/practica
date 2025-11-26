#Programa49
encontrada=0
palabra=input("Introduce la palabra secreta: ")
for i in range(len(palabra)):
    letra=input("Introduce una letra: ")
    encontrada=0
    for i in range(len(palabra)):
        if palabra[i]==letra:
            print(f"la letra se encuentra en la posición {i+1}")
            encontrada=1
    if encontrada==0:
        print("la letra no se encuentra en ninguna posición")



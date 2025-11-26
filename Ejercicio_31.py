#Programa31
print("A quién madruga Dios ayuda.")
frase=("A quién madruga Dios ayuda.")
palabra=input("Introduce una palabra del frace: ")
indice=frase.find(palabra)
if indice != -1:
    print(f"La palabra está en la frase y está en el índice: {indice}.")
else:
    print(f"La palabra {palabra} no está en la frase.")

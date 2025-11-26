#Programa32
print("A quién madruga Dios ayuda.")
frase=("A quién madruga Dios ayuda.")
palabra=input("Introduce una palabra del frace: ")
frase_en_minusculas=frase.lower()
palabra_en_minusculas=palabra.lower()
indice=frase_en_minusculas.find(palabra_en_minusculas)
if indice != -1:
    print(f"La palabra '{palabra}' se encuentra en el índice {indice}")
else:
    print(f"La palabra '{palabra}' no se encuentra en la frase.")

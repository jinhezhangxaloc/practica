#Programa33
def vocal_a(frase):
    vocal_a = "aáà"
    frase_en_minusculas = frase.lower()
    contador = 0
    for letra in frase_en_minusculas:
        if letra in vocal_a:
            contador += 1
    return contador
frase = "No hay mal que dure cien años"
numero_de_vocales_a = vocal_a(frase)

def vocal_e(frase):
    vocal_e = "eéè"
    frase_en_minusculas = frase.lower()
    contador = 0
    for letra in frase_en_minusculas:
        if letra in vocal_e:
            contador += 1
    return contador
frase = "No hay mal que dure cien años"
numero_de_vocales_e = vocal_e(frase)

def vocal_i(frase):
    vocal_i = "iíì"
    frase_en_minusculas = frase.lower()
    contador = 0
    for letra in frase_en_minusculas:
        if letra in vocal_i:
            contador += 1
    return contador
frase = "No hay mal que dure cien años"
numero_de_vocales_i = vocal_i(frase)

def vocal_o(frase):
    vocal_o = "oóò"
    frase_en_minusculas = frase.lower()
    contador = 0
    for letra in frase_en_minusculas:
        if letra in vocal_o:
            contador += 1
    return contador
frase = "No hay mal que dure cien años"
numero_de_vocales_o = vocal_o(frase)

def vocal_u(frase):
    vocal_u = "uúù"
    frase_en_minusculas = frase.lower()
    contador = 0
    for letra in frase_en_minusculas:
        if letra in vocal_u:
            contador += 1
    return contador
frase = "No hay mal que dure cien años"
numero_de_vocales_u = vocal_u(frase)

print(f"La frase es: '{frase}'")
print(f"El número de a es {numero_de_vocales_a} el número de e es {numero_de_vocales_e} el número de i es {numero_de_vocales_i} el número de o es {numero_de_vocales_o} y el número de u es {numero_de_vocales_u} ")

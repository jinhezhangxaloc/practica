#for
# Uso principal: Iterar sobre una secuencia (listas, tuplas, cadenas, rangos, etc.).
# Número de iteraciones: Se conoce de antemano (o está determinado por la longitud de la secuencia).

# for → Ideal para recorrer colecciones o rangos definidos.
# while → Ideal para bucles que dependen de una condición que puede cambiar dinámicamente.


#for elemento in secuencia:
    #bloque de código

for i in range(5):
    print(i, "valor") #imprime 0,1,2,3,4

for i in range(0,10):
    print(i)

for i in range(0,10,2):
    print(i)

suma_total=0
repeticiones = int(input("Introduce un valor"))
for i in range(repeticiones):
    print(i)
    suma_total=suma_total+i
print(suma_total)

password="Contr@s.=2025T"
for i in range(len(password)):
    print(password[i])

password="Contr@s.=2025T"
for i in range(len(password)):
    if password[i].isnumeric():
        print(password[i])
    else:
        print("No és numérico")


#Recorrer un string carácter a carácter
password="Contr@s.=2025T"
for i in password:
    print(i)
#while
# Uso principal: Repetir mientras se cumpla una condición lógica.
# Número de iteraciones: No necesariamente se conoce; depende de cuándo la condición deje de ser verdadera.

# while condicion:
    #bloque de código

contador = 0
while contador < 5:
    print(contador)
    contador += 1

###Ejercicios

#Ejer 1:   Sumar el total de los caracteres que sean numéricos
#Ejer 2:   Determinar el número de vocales
###     Pista vocales="aeiouAEIOU"
###     if i in vocales:



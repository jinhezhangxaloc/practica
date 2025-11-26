#Programa39 
positivos=0
negativos=0
ceros=0
cantidad=int(input("Introduce la cantidad de números que deseas introducir: "))
for i in range(cantidad):
    numero=float(input("Introduce un número: "))
    if numero>0:
        positivos+=1
    elif numero<0:
        negativos+=1
    else:
        ceros+=1
print(f"La cantidad de números positivos és: {positivos}")
print(f"La cantidad de números negativos és: {negativos}")
print(f"La cantidad de números ceros és: {ceros}")



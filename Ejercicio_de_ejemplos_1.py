#Practica1
frace=(input("Introduce cualquiera frace "))
suma=0
for i in frace:
    if i.isnumeric():
        suma+=int(i)
print(f"La suma total de los números de este frace és: {suma}")



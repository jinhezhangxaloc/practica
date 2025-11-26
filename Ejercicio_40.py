#Programa40 
pares=0
impares=0
numero=int(input("Introduce un números "))
for i in range(1, numero):
    if i % 2==0:
        pares+=1
    else:
        impares+=1
print(f"El total de pares és: {pares}")
print(f"El total de impares és: {impares}")



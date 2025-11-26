#Programa47
intervalo1=int(input("Introduce el primer intervalo: "))
intervalo2=int(input("Introduce el segundo intervalo: "))
if intervalo1<intervalo2:
    for i in range(intervalo1, intervalo2+1):
        if i!=intervalo2:
            print(f"{i}-", end="")
        else:
            print(i)
else:
    for i in range(intervalo1, intervalo2-1,-1):
        if i!=intervalo2:
            print(f"{i}-", end="")
        else:
            print(i)


#Programa42
numero=int(input("Introduce el número de simbolos que hay en el patron más largo "))
for i in range(1, numero+1):
    print("*" * i)
for i in range(numero-1, 0, -1):
    print("*" * i)


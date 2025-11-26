#Programa41
numero=int(input("Introduce el número más grande del patron "))
for i in range(numero, 0, -1):      
    for i in range(i, 0, -1):  
        print(i, end="")       
    print()    



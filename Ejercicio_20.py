#Programa20
var1=int(input("Introduce el primero numero "))
var2=int(input("Introduce el segundo numero "))
if var1 > 10 or var2 > 10 :
    print("Uno o los dos números están fuera de los límites establecidos") 
elif var1 == var2: 
    print("Ambos números son iguales.") 
elif var1 > var2: 
    print(f"El número {var1} es mayor que el número {var2}") 
elif var1 < var2: 
    print(f"El número {var2} es mayor que el número {var1}") 
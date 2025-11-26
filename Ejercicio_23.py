#Programa23
var1=float(input("Introduce la nota que has sacado "))
if var1 > 10 or var1 < 0 :
    print("La nota que has introducido no está entre 0 y 10") 
elif var1 == 8.5 or var1 > 8.5 : 
    print(f"Tu nota es un {var1}, has sacado un excelente") 
elif var1 == 6.5 or var1 > 6.5 : 
    print(f"Tu nota es un {var1}, has sacado un notable") 
elif var1 == 5 or var1 > 5 : 
    print(f"Tu nota es un {var1}, has sacado un satisfactorio") 
elif var1 < 5 : 
    print(f"Tu nota es un {var1}, has sacado un insuficiente") 


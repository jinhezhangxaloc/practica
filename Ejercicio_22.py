#Programa22
var1=float(input("Introduce la nota que has sacado "))
if var1 > 10 or var1 < 0 :
    print("La nota que has introducido no está entre 0 y 10") 
elif var1 == 5 or var1 > 5 : 
    print(f"Has sacado un {var1} y has aprobado") 
elif var1 < 5: 
    print(f"Has sacado un {var1} y has suspendido") 
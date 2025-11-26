#Programa24
var1=float(input("Introduce el peso (en KM): "))
var2=float(input("Introduce la altura (en metros): "))
var_imc=var1/(var2**2)
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es:", var_imc)
if var_imc>25 or var_imc==25:
    print("Hay sobrepeso")
else:
    print("Estás dentro de los parámetros normales")
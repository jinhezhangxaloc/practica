#Programa21  
import math   
a=float(input("Introduce el numero A de una ecuación de segundo grado "))  
b=float(input("Introduce el numero B de una ecuación de segundo grado "))  
c=float(input("Introduce el numero C de una ecuación de segundo grado "))  
if (b**2) > (4*a*c): 
    resultado1=float(float(-b)+math.sqrt(float(b**2)-float(4*a*c)))/2*a  
    resultado2=float(float(-b)-math.sqrt(float(b**2)-float(4*a*c)))/2*a  
    print(f"El valor de x1 es:", resultado1)   
    print(f"El valor de x2 es:", resultado2)   
else: 
    print("La raíz no puede ser un valor negativo") 
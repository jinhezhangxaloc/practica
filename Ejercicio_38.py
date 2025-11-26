#Programa38 
numero_de_nota=input("Introduce el número de notas que deseas introducir: ")
if numero_de_nota.isdigit():
    for i in range(int(numero_de_nota)):
        nota=float(input("Introduce la nota: "))
        if nota>=10:
            print("Has introducido una nota equivocada")
        if nota<=0:
            print("Has introducido una nota equivocada")
        else:
            if nota<=5:
                print("Asignatura suspendida")
            else:
                print("Asignatura aprobada")
else:
    print("Error")



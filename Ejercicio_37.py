#Programa37   
numero_de_nota=input("Introduce el número de notas que deseas introducir: ")
if numero_de_nota.isdigit():
    for i in range(int(numero_de_nota)):
        nota=float(input("Introduce la nota: "))
        if nota>=5:
            print("Asignatura aprobada")
        else:
            print("Asignatura suspendida")
else:
    print("Error")

    
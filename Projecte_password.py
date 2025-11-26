# Projecte password  
print("Les condicions que ha de complir la contraseny són")  
print("-Posició 1: Un numero major o igual 1 i menor o igual que 5 (1-5).")  
print("-Posició 2: Una lletra minúscula (a-z). ")  
print("-Posició 3: Una lletra majúscula (A-Z). ") 
print("-Posició 4: Un dels següents símbols *, _, @. ")  
print("-Posició 5: Una lletra minúscula (a-z). ")  
print("-Posició 6: Un número major o igual 6 i menor o igual que 9 (6-9). ")  
print("-Posició 7: Un dels següents símbols &, /, #. ")  
print("-Posició 8: Un numero menor o igual que 5 (0-5). ") 
password=input("Introdueix el teu password: ")  
longitud=len(password)  
errors=[]  
if longitud < 6 or longitud > 8:  
    print(f"Error, el password té una longitud de {longitud} caràcters i no compleix els requisits")  
else: 
    if not (password[0].isdigit() and 1<=int(password[0])<=5): 
        errors.append(f" ''Error en el caràcter 1''")  
    if not (password[1].islower()):  
        errors.append(f" ''Error en el caràcter 2''")  
    if not (password[2].isupper()):  
        errors.append(f" ''Error en el caràcter 3''")  
    if password[3] not in ["*", "_", "@"]:  
        errors.append(f" ''Error en el caràcter 4''")  
    if not (password[4].islower()): 
        errors.append(f" ''Error en el caràcter 5''")  
    if not (password[5].isdigit() and 6<=int(password[5])<=9):  
        errors.append(f" ''Error en el caràcter 6''")  
    if longitud>=7 and password[6] not in ["&", "/", "#"]: 
        errors.append(f" ''Error en el caràcter 7''")  
    if longitud==8 and not (password[7].isdigit() and 0<=int(password[7])<=5):  
        errors.append(f" ''Error en el caràcter 8''")  
    if len(errors)==0:  
        print("El format del PASSWORD és correcte")  
    else:  
        print("".join(errors))  
        
    
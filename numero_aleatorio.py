import random 
numero_aleatorio=random.randint(1,10)
print("usted tiene 3 intentos ")
introducir_numero=int(input("introduzca el numero de 1-10 : "))
if introducir_numero>numero_aleatorio:
    print("Es menos")
elif introducir_numero<numero_aleatorio:
    print("Es mayor")
else:
    introducir_numero==numero_aleatorio
    print("has acertado el juego ha terminado")
    
introducir_numero=int(input("introduzca el numero de 1-10 : "))
print("usted tiene 2 intentos ")
if introducir_numero>numero_aleatorio:
    print("Es menos")
elif introducir_numero<numero_aleatorio:
    print("Es mayor")
else:
    introducir_numero==numero_aleatorio
    print("has acertado el juego ha terminado")
    
introducir_numero=int(input("introduzca el numero de 1-10 : "))
print("usted tiene 1 intentos ")
if introducir_numero>numero_aleatorio:
    print("Es menos")
elif introducir_numero<numero_aleatorio:
    print("Es mayor")
else:
    introducir_numero==numero_aleatorio
    print("has acertado el juego ha terminado")    
 
print ("PERDISTE")           
    


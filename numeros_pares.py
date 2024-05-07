numero=int(input("introduzca numero entero positivo: "))
suma_pares=0
lista=[]
for i in range (1,numero):
    if i%2==0:
        suma_pares+=i
        lista.append(i)
        
        
print("suma de los numeros pares",suma_pares)
print("lista de numeros pares hasta numero", lista)
print("conteo de la lista de numeros pares",len(lista))

        
    
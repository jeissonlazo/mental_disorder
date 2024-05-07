numero = int(input('Introduzca el número: '))
lista=[]
for i in range(2,numero):
    es_primo=True
    for j in range(2,i):
        if i%j  == 0:
            es_primo=False
            break
    if es_primo:
        lista.append(i)
            
    
print(' numeros primos hasta numero introducido:',lista)
        
        
         
        
   
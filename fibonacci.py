#variable input,en la cual se introducira un numero entero ese numero sera los  "n" terminos de la serie fibonacci
n=int(input("introduzca numero entero; "))

# variable fibonacci,tendra los primeros 2 terminos,apartir de esos terminos se empezara a hacer la suma hasta n 
fibonacci=[0,1]

#bucle for para empezar a hacer la suma con los dos ultimos terminos para sacar el nuevo termino 
# asi sucesivamente hasta "n" terminos

for i in range(2,n):
    nuevos_valores = fibonacci[-1] + fibonacci[-2]
    # los valores devueltos por el bucle los introducimos en la variable fibonacci con ".append"
    fibonacci.append(nuevos_valores)
    
print("la serie fibonacci es ",fibonacci)
numero_romano=str(input("introduzca los numeros romanos (I),(V),(X),(L),(C),(D),(M): "))
valores_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
resultado_decimal=0
# bucle for para coger cada letra del numero romano introducido y se almacene cada iteracion en i
for i in range(len(numero_romano)):
    #Se está obteniendo el valor numérico asociado al símbolo romano actual= "valores_romanos[numero_romano[i]]""
    ## y se añade y suma a la variable resultado_decimal "+="
    resultado_decimal += valores_romanos[i]
        

print("El número decimal equivalente es:", resultado_decimal)
    
    



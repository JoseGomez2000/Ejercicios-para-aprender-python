"""
Crea un programa que:

Pida al usuario que ingrese 5 números (uno por uno).
Guarde esos números en una lista llamada numeros.
Usando un for, recorra la lista e imprima:
Todos los números
La suma total de los números
El número más grande y el más pequeño
"""

#el codigo es funcional pero es erroneo en la siguiente practica se
#simplifica con un enfoque mas logico y cambieando la manera en que se debe de hacer

numeros = []
contador = 5
contadorr = 1
#aca tenemos la idea principal 
#nuevo_numero = numeros.append(int(input("ingrese un numero : ")))

#print(numeros)

for i in range(int(contador)): 
    nuevo_numero = numeros.append(int(input("ingrese un numero : ")))
    i += 1

for j in range(int(contadorr)): 
    print(f"\nNumeros agregados a la lista\n{numeros}")
    suma_lista = sum(numeros)
    print(f"la suma de la lista es: {suma_lista}")
    print(f"El numero menor es: {(min(numeros))}")
    print(f"El numero con el valor mas alto es: {(max(numeros))}")
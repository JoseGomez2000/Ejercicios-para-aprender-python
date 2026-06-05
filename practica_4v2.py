"""
Crea un programa que:

Pida al usuario que ingrese 5 números (uno por uno).
Guarde esos números en una lista llamada numeros.
Usando un for, recorra la lista e imprima:
Todos los números
La suma total de los números
El número más grande y el más pequeño
"""

#ERROR usar 2 for y variables que se nombraron contador para el limite del for.
#enfoque del append es bueno pero mal ejecutado.
#el uso de sum,max,min es bueno pero es mejor mostrar todo el proceso
#falto el uso de while con try-except
numeros = []

print("Ingresa 5 numeros:\n") 

for i in range(5):
    while True:
        try:
            num = int(input(f"Ingrese el numero {i+1}; "))
            numeros.append(num)
            break
        except ValueError:
            print("ERROR: Ingrese solo numero")

print("===============")
print(f"Numeros agregados: {numeros}")

suma = sum(numeros)
mayor= max(numeros)
menor= min(numeros)

print(f"La suma total es: {suma}")
print(f"El numero mayor es: {mayor}")
print(f"el numero menor es: {menor}")

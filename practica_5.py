"""Crea un programa que:

Pregunte cuántos términos de la serie Fibonacci quiere ver (mínimo 5, máximo 20).
Usando un for, genere y muestre la cantidad de términos de la serie Fibonacci que pidió.
"""
#uso dos variables tipo entero para iniciar la sucesión de Fibonacci es una secuencia infinita 
#de números donde cada número se obtiene sumando los dos números anteriores.
a = 0
b = 1
#manejar el error que puede ocasionarse al momento de ingresar la cantidad
while True:
    try: #pedir el numero de repeticiones para ingresarla en un ciclo for
        num = int(input("Ingrese un numero para mostras la secuencia de fibonaci(5 min-20 max): "))
        if 5 <= num <= 20: #manejar el rango en el que se desea trabajar
            break
        else: 
            print("El numero no esta dentro del rango.")
    except ValueError:
        print("ERROR: Digite una cantidad numerica.")
#ingresar la vaiable que obtuvimos y hacer el recorrico 
for i in range(num):
    print(a, end="\n") #imprimir los valores de los calculos 
    a, b = b, a + b
#En esta linea del codigo es simple pero a la vez complicado de entender 
#a, b = b, a + b lo que pasa aca es que python entiende de una manera esa line de lado derecho 
#a izquierdo seria de esta manera (a,b) = (b, a+b), esto se interpreta de la siguiente manera de 
#derecha a izquierda, dode b(derecha) toma el valor de a(izquierda) y el siguiente a+b(derecha) 
#tomara el valor de b(izquierda) hay mas maneras de representarlas pero esta es una de las mas eficientes.
#  
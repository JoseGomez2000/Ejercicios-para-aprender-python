#Crea un programa que:

#Pregunte al usuario un número entero positivo (ej: 10).
#Usando un for, imprima la tabla de multiplicar de 
#ese número del 1 al 10.

multiplicadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    try: 
        numero = int(input("escriba un numero entero positivo: "))
        if numero > 0:
            break
        else:
            print("El numero ingresado no es positivo ingrese otro numero valido.")
    except ValueError:
        print("ERROR: el valor ingresado no es un numero, ingrese un numero valido")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
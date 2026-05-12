"""
Tema: Bucles, validación de datos y cálculos
Enunciado:
Mejora el programa anterior haciendo lo siguiente(practica_1):

1.-El programa debe validar que la edad sea un número entero positivo 
(entre 0 y 120 años). Si el usuario ingresa algo inválido, debe volver
a pedir la edad hasta que sea correcta.
2.-Una vez que tenga el nombre y la edad válida, debe preguntar cuántas 
veces quiere que se repita el mensaje de saludo (mínimo 1, máximo 5).
3.-Usando un bucle for o while, imprime el saludo completo 
(nombre + edad + mensaje de etapa de vida + años para los 100) 
las veces que el usuario indicó.

Pista: Usa try-except para manejar errores de conversión cuando el 
usuario no ingrese un número.
"""

#inicio de codigo.
nombre = input("Ingrese su nombre: ")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if 0 <= edad <= 120:
            break
        else:
            print("El rango de edad debe de ser del 0 al 120")
    except ValueError:
        print("ERROR: ingrese numero validos")
edad_faltante = 100 - edad

#veces en las que se repite el saludo de 1 a 5 veces 

while True:
    try:
        repetir_saludo = int(input("ingrese cuantas veces quiere ver el saludo:"))
        if 1 <= repetir_saludo <= 5:
            break
        else: 
            print("valor no valido ingrese un numero del 1 al 5")
    except ValueError:
        print("ERROR: el valor que ingreso no es numerico ingrese un valor valido 1-5")
#saludo en un ciclo for
for i in range(repetir_saludo):
    print(f"Mensaje {i+1}:")
    print(f"Nombre: {nombre}, tienes {edad} años")

    if edad <18:
        etapa = "Eres menor de edad"
    elif edad <= 30:
        etapa = "Estas en la juventud"
    elif edad <= 60:
        etapa = "Estas en la adultez"
    else:
        etapa = "Eres un adulto mayor"
        
    print(etapa)
    print(f"te faltan {edad_faltante} años para alcanzar la edad de 100 años")

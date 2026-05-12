"""
Tema:Estructuras condicionales + cálculos simples
Enunciado:
Crea un programa que pida al usuario su nombre y su edad.
Luego debe mostrar lo siguiente:

El saludo personalizado como en el ejemplo.
Dependiendo de la edad, debe mostrar un mensaje diferente:
Si es menor de 18 años → "Eres menor de edad."
Si tiene entre 18 y 30 años → "Estás en la juventud."
Si tiene entre 31 y 60 años → "Estás en la adultez."
Si tiene más de 60 años → "Eres un adulto mayor."

Además, calcula y muestra cuántos años le faltan para cumplir 100 años.
"""

#inicio de codigo

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
#f-string se usa para ingresar directamente variables.
print(f"Bienvenido {nombre}, tienes una edad de {edad} años")

if edad < 18:
    print("Eres menor de edad")
elif edad<= 30:
    print ("Estas en la juventud")
elif edad <= 60:
    print("Estas en la adultez")
else:
    print("Eres un adulto mayor")

edad_calculada = 100 - edad
print(f"Te faltan :{edad_calculada}, años para tener 100 años")
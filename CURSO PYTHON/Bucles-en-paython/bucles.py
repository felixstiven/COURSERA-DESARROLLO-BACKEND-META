#Escenario
#Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number.
#Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos.
#¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

#Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

#pedirá al usuario que ingrese un número entero;
#utilizará un bucle while;
#comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."

#¡El mago está contando contigo! No lo decepciones.



print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
secret_number = 777



entrada_numero = int(input("ingresa un numero entero para adivinar el numero secreto del mago"))

while entrada_numero:
    
   if secret_number != entrada_numero:
      print("jaja estas en un bucle infinito")

   if secret_number == entrada_numero:
      print ("eres un genio encontraste el numero")
      break
print()

#BUCLES CON FOR

#Echemos un vistazo a un programa corto cuya tarea es escribir algunas de las primeras potencias de 2 =

power = 1

for exp in range(10):
   print (" 2 a la potencia de ", exp, "es", power)
   power *=2

pritnt ()

#3.2.7   LAB   Fundamentos del bucle for – (break y continue)
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
print()

#Las sentencias break y continue: más ejemplos
#Regresemos a nuestro programa que reconoce el más grande entre los números ingresados.
#Lo convertiremos dos veces, usando las instrucciones de break y continue.

#Analiza el código y determina como las usarías.

#la variante empleando break es la siguiente:

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
print ()



































































   



  

           

    
    



#ESTE ES UN CURSO BASICO CONTIENE MODULO 1 Y MODULO 2 VARIABLES/OPERACIONES ARIMETICAS/BOLEANOS/Palabras claves de covertir nunmeros 
print ("hissss....")


print ("vino la lluvia y se llevo todo\nsubio a su.")
print ()
print ("todo se fue con ella\ny se la llevo")

print ()

print ("mi nombre es " , end="")
print ("felix alvis")

print ()

print ("Mi", "nombre", "es", "stiven", "felix", sep="-")

print ()

print ("Mi", "nombre", "es", sep="_", end="*")
print ("stiven", "felix", sep="*", end="*")


print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)

print()

print (" mi nombre es \"stiven felix\"")
print()
print (" \"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"python\"\"\" ")

print ()

#variables en python
print ("variables en python")
print()
var = 1
account_balance = 1000.0
cliente_name = "Jhon doe"
print (var, account_balance, cliente_name)
print (var)
#OPERADORES EN PYTHON
print()
print("convertidor de dolar a pesos y de peso a dolar")

pesos = 8000
dolar = 2.5

pesos_to_dolar = pesos / 5000
dolar_to_pesos = dolar * 5000
print (pesos, "pesos son", round(pesos_to_dolar, 2), "dolares")
print (dolar, "dolares son", round(dolar_to_pesos, 2), "pesos")

#FUNCION INPU() RECOJE DATOS DEL USUARIO PARA PODER HACER FUNCIONAR EL PROGRAMA
print("HOLA COMO ESTAS...")
anything = input()
print("Hmm...", anything, "... ¿QUE BUENO  BUEN DIA?")
#Nota:función input() se invoca con un argumento: es una cadena que contiene un mensaje;
#el mensaje se mostrará en la consola antes de que el usuario tenga la oportunidad de ingresar algo;
#input() entonces hará su trabajo.
#Esta variante de la invocación de input() simplifica el código y lo hace más claro.

Anything = input("¿como estas?..")
print (Anything, "que tengas buen dia")

#PARA REALIZAR OPERACIONES CON INPUT SE DEBE UTILIZAR OTTRAS FUNCIONES PRIMERO
#INT()CONVIERTE EL NUMERO INGRESADO QUE A NUMERO ENTERO
#FLOAT() CONVIERTE EL NUMERO STRING INGRESADO A NUMERO FLOTANTE
#EJEMPLOS

anything = float(input("ingresa el numero que quieres exponenciar a las 2.."))
something = anything **2
print(anything, "a la potencia de 2 es", something)

#vamos a realizar un ejercicio de hipotenusa

leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print ("la longitud de la hipotenusa es: ", hypo)

#pedir datos utilizando el operador + pero para concatenar string ejemplo

firts_name = input("inngresa tu primer nombre")
firts_family = input ("ingresa tu primer apellido")
print ("GRACIAS")
print("/nTu nombre es: " + firts_name + " " + firts_family + ".")
print()

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
 



















 




























  

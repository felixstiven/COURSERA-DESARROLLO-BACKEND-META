print ("siguiendo el curso de python")
# operador igual a (==)
var = 0  # Asignando 0 a var
print(var == 0)

var = 1  # Asignando 1 a var
print(var == 0)
print()

#operador Desigualda no es igua a (!=)
var = 0  # Asignando 0 a var
print(var != 0)
 
var = 1  # Asignando 1 a var
print(var != 0)

#sentencias y condiciones de if else
print ()

number1 = int(input("ingresa el primer numero"))
number2 = int(input("ingrese el segundo numero"))

if number1 > number2:
    larger_number = number1

else:
    larger_number = number2

print ("El numero mas grande es: ", larger_number)
print ()

#Python a menudo viene con muchas funciones integradas que harán el trabajo por ti. Por ejemplo,
#para encontrar el número más grande de todos, puede usar una función incorporada de Python llamada max().
#Puedes usarlo con múltiples argumentos. Analiza el código de abajo:
# se puede utilizar la funcion min tambien para bucar el menor 

number1 = int(input("ingresa el primer numero"))
number2 = int(input("ingrese el segundo numero"))
number3 = int(input("ingresa el tercer numero"))

largers_number = max(number1, number2, number3)

print ("el numero mayor es : ", largers_number)
print()

#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:
#imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!"
#en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
#imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
#imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

entrada = input("ingrese palabra de la planta : " )


if entrada == "ESPATIFILO" :
    print ("!Espatifilo es la mejor planta de todas!")
if entrada == "espatifilo" :
    print ("no me gusta esa planta")
if entrada != "ESPATIFILO" :
    print (entrada, "no es el nombre correcto de la planta")
print ()

#Escenario
#Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

#si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
#si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
#Tu tarea es escribir una calculadora de impuestos.

#Debe aceptar un valor de punto flotante: el ingreso.
#A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
#Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

#Observa el código en el editor - solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes.

#Prueba tu código con los datos que hemos proporcionado.

#mi codigo
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Escribe tu código aquí.
if income > 85528 :
    tax = (income - 85528) * 0.32 + 14832.02

if if tax < 0.0:
	tax = 0.0
	
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
print()
    




























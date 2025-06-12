print("TALLER DE CONDICIONALES Y DIAGRAMAS DE FLUJOS")

print("---Ejercicios con Condicionales y Operaciónes Matemáticas---")

print("Ejercicio 1: Verifica si un número es positivo, negativo o cero")
num1=float(input("Ingrese un número: "))
if num1 > 0:
    print("El número es positivo")
elif num1 < 0:
    print("El número es negativo")
else:
    print("El número es cero")


print("Ejercicio 2:  Calcula el mayor de dos números ingresados")
num2a=float(input("Ingresa el primer número: "))
num2b=float(input("Ingresa el segundo número: "))
if num2a > num2b:
    print("El número mayor es:", num2a)
else:
    print("El número mayor es:", num2b)


print("Ejercicio 3: Determina si un número es par o impar")
num3=int(input("Ingrese un número: "))
if num3 % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


print("Ejercicio 4: Dado un número, verifica si está entre 10 y 20")
num4=int(input("Ingrese un número: "))
if num4>= 10 and num4<=20:
    print("El número está entre 10 y 20")
else:
    print("El número no está entre 10 y 20")


print("Ejercicio 5: Dados tres números, encuentra el mayor usando condicionales")
num5a=float(input("Ingresa el primer número: "))
num5b=float(input("Ingresa el segundo número: "))
num5c=float(input("Ingresa el tercer número: "))

if num5a>=num5b and num5a>=num5c:
    print("El número mayor es:", num5a)
elif num5b>=num5a and num5b>=num5c:
    print("El número mayor es:", num5b)
else:
    print("El número mayor es:", num5c)
    

print("Ejercicio 6: Calcula el precio final con un 10% de descuento si el total es mayor a $100")
precio6=float(input("Ingrese el precio de tu producto: "))

if precio6>100:
    des6a=precio6*10/100
    des6b=precio6-des6a
    print("El precio final con descuento es:", des6b)
else:
    print("Debido a que el precio es menor a 100, no se aplica descuento. El precio final es:", precio6)


print("Ejercicio 7: Verifica si una persona puede votar (mayor o igual a 18 años)")
edad7=int(input("Ingrese su edad: "))
if edad7 >= 18:
    print("Usted puede votar")
else:
    print("Usted no puede votar")


print("Ejercicio 8: Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP")
precio8=float(input("Ingrese el precio del producto: "))
tipcli8=input("Ingrese el tipo de cliente (VIP o normal): ")

if tipcli8.upper() == "VIP":
    des8a=precio8*20/100
    des8b=precio8-des8a
    print("El precio final con descuento es:", des8b)
else:
    print("Debido a que no es cliente VIP, no se le aplica descuento. El precio final es:", precio8)
    
print("Ejercicio 9: Determina si un número es múltiplo de 5 y de 3 al mismo tiempo")
num9=int(input("Ingrese un número: "))
if num9 % 5 == 0 and num9 % 3 == 0:
    print("El número es múltiplo de 5 y de 3")
else:
    print("El número no es múltiplo de 5 y de 3 al mismo tiempo")

print("Ejercicio 10: Dado un número, verifica si es divisible entre dos números dados")
num10=int(input("Ingrese un número: "))
divi10a=int(input("Ingrese el primer divisor: "))
divi10b=int(input("Ingrese el segundo divisor: "))
if num10 % divi10a == 0 and num10 % divi10b == 0:
    print("El número es divisible entre", divi10a, "y", divi10b)
else:
    print("El número no es divisible entre", divi10a, "y", divi10b)
    

print("---Ejercicios con Listas (con condicionales)---")

print("Ejercicio 11: Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”")
numeros11 = []

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
num11=[1,2,3,4,5]
print("La lista es: ",num11)

if num11[2] > 10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10")
    

print("Ejercicio 12: Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.")
lst12=[3,5,7,9]

if 7 in lst12:
    print("Está en la lista")
else:
    print("No está en la lista")
    
    
print("Ejercicio 13: Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.")
lst13=[4,6,2,8]
if  lst13[0]+lst13[1] >10:
    print("Suma alta")
else:
    print("Suma baja")


print("Ejercicio 14: Dada la lista  [Ana, Luis, Pedro, Marta] muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente")
lst14=["Ana","Luis","Pedro","Marta"]

if lst14[3] == "Marta":
    print("Nombre corecto")
else:
    print("Nombre diferente")
    

print("Ejercicio 15: Crea una lista con tres colores. Cambia el segundo color solo si es igual a azul, y muestra la lista actualizada.")
lst15=["Blanco","Azul","Rosado"]
print("La lista es: ",lst15)
 
if lst15[1].lower() == "azul":
    lst15[1] = "Rojo"
    print("La lista actualizada es:", lst15)
else:
    print("El segundo color no es azul, la lista permanece igual:", lst15)
    
    

print("---Ejercicios con Tuplas (con condicionales)---")

print("Ejercicio 16: Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”")
t16=(5,8,12,20)

if t16[0]<t16[-1]:
    print("Orden ascendente")
else:
    print("Orden descendente")


print("Ejercicio 17: Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.")
t17=(25,32,28)
if t17[1]>30:
    print("Edad mayor a 30")
else:
    print("Edad menor o igual a 30")
    

print("Ejercicio 18: Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.")
t18=(1,2,3)
print("La tupla es: ",t18)
t_lst18=list(t18)
print("Ahora la tupla convertida en lista es: ",t_lst18)

if t_lst18[1]==2:
    t_lst18[1]=10  # Cambiar el segundo valor
    lst_t18=tuple(t_lst18)
    print("Ahora la lista convertida en tupla es: ",lst_t18)
else:
    print("El segundo valor no es 2, la tupla permanece igual:", t18)


print("Ejercicio 19: Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.")
t19=(4,9)
if t19[1]>5:
    print("Coordenada alta")
else:
    print("Coordenada baja")


print("Ejercicio 20: Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”.")
ta20=(3,4)
print("La tupla 1 es: ",ta20)
tb20=(3,5)
print("La tupla 2 es: ",tb20)

if ta20==tb20:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")
    


print("---Ejercicios con Diccionarios (con condicionales)---")

print("Ejercicio 21: Crea un diccionario con ""nombre:Juan, edad: 17"". Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.")
dic21={
    "nombre": "Juan",
    "edad": 17
}

if dic21["edad"] >= 18:
    print("Adulto")
else:
    print("Menor de edad")


print("Ejercicio 22: Crea un diccionario ""nombre:Lucía,edad: 20"" Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario")
dic22={
    "nombre":"Lucía",
    "edad":20
}
print("El diccionario es: ",dic22)

if dic22["edad"] > 18:
    dic22["edad"]=21
    print("El diccionario modificado es: ",dic22)
else:
    print("La edad no es mayor a 18, el diccionario permanece igual:", dic22)


print("Ejercicio 23: Crea un diccionario con nombre: Carlos. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario. ")
dic23={
    "nombre":"Carlos",
}

if "ciudad" not in dic23:
    dic23["ciudad"] = "Bogotá"
    print("Diccionario actualizado:", dic23)
else:
    print("La clave 'ciudad' ya existe en el diccionario:", dic23)


print("Ejercicio 24: Dado el diccionario producto:pan,precio: 1200, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”")
dic24={
    "producto":"pan",
    "precio":1200
}

if "precio" in dic24:
    print(dic24["precio"])
else:
    print("No hay precio")


print("Ejercicio 25: Crea un diccionario con pan: 1200, leche: 2000. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible")
dic25={
    "pan":1200,
    "leche":2000
}

if "pan" in dic25:
    print(dic25["pan"])
else:
    print("Producto no disponible")
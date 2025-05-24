print("-----EJERCICIO 1: Registrar frutas-----")
frutas=[] #Lista vacia para agragar cosas luego
frutas.append(input("Ingresa la primera fruta: "))
frutas.append(input("Ingresa la segunda fruta: "))
frutas.append(input("Ingresa la tercera fruta: "))

print("Las frutas registradas son:", frutas)

print("-----EJERCICIO 2: Guardar 2 edades-----")
edad=[]
edad.append(int(input("Ingrasa tu edad hace 3 años: ")))
edad.append(int(input("Ingresa tu edad actual: ")))

print("Las edades almacenadas son: ",edad)


print("-----EJERCICIO 3: Notas de dos estudiantes-----")
notas=[]

notas.append(float(input("Ingresa la primera nota: ")))
notas.append(float(input("Ingresa la segunda nota: ")))

prom=(notas[0]+notas[1])/2

print("El promedio de las notas es: ",prom)


print("-----EJERCICIO 4: Productos en una bolsa-----")
productos=[]

productos.append(input("Ingresa el nombre del producto 1: "))
productos.append(input("Ingresa el nombre del producto 2: "))
productos.append(input("Ingresa el nombre del producto 3: "))

print("Los productos en la bolsa son:", productos)


print("-----EJERCICIO 5: Precios de 3 artículos-----")
precios=[]

precios.append(float(input("Ingresa el precio del artículo 1: ")))
precios.append(float(input("Ingresa el precio del artículo 2: ")))
precios.append(float(input("Ingresa el precio del artículo 3: ")))

sum=precios[0]+precios[1]+precios[2]


print("La suma total de los precios es: ",sum)


print("-----EJERCICIO 6: Números ingresados por el usuario-----")
numeros=[]

numeros.append(float(input("Ingresa el número 1: ")))
numeros.append(float(input("Ingresa el número 2: ")))
numeros.append(float(input("Ingresa el número 3: ")))
numeros.append(float(input("Ingresa el número 4: ")))

max=max(numeros)
men=min(numeros)

print("El número mayor es: ",max)
print("El número menor es: ",men)


print("-----EJERCICIO 7: Registrar dos nombres completos-----")
nombres=[]

nombres.append(input("Ingresa el primer nombre completo: "))
nombres.append(input("Ingresa el segundo nombre completo: "))

print("Hola,", nombres[0])
print("Hola,", nombres[1])


print("-----EJERCICIO 8: Registrar dos temperaturas-----")
temperaturas=[]

temperaturas.append(float(input("Ingresa la primera temperatura en °C: ")))
temperaturas.append(float(input("Ingresa la segunda temperatura en °C: ")))

f1=(temperaturas[0]*9/5)+32
f2=(temperaturas[1]*9/5)+32

print("Las temperturas convertidas en Fahrenheit son: ",f1," y ",f2)
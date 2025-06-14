print("------------------------ejercicio 1------------------------")
num11=int(input("Ingresa el primer número: "))
num21=int(input("Ingresa el segundo número: "))

resultado1=num11+num21
print("El resultado de la suma es: ", resultado1)


print("------------------------ejercicio 2------------------------")
num12=int(input("Ingresa el primer número: "))
num22=int(input("Ingresa el segundo número: "))

resultado2=num12-num22
print("El resultado de la resta es: ", resultado2)


print("------------------------ejercicio 3------------------------")
num13=int(input("Ingresa el primer número: "))
num23=int(input("Ingresa el segundo número: "))

resultado3=num13*num23
print("El resultado de la multiplicación es: ", resultado3)


print("------------------------ejercicio 4------------------------")
num14=int(input("Ingresa el primer número: "))
num24=int(input("Ingresa el segundo número: "))

resultado4=num14/num24
print("El resultado de la división es: ", resultado4)


print("------------------------ejercicio 5------------------------")
nomb5=input("Ingresa tu nombre: ")
apel5=input("Ingresa tu apellido: ")

print("Hola "+nomb5+" "+apel5)


print("------------------------ejercicio 6------------------------")
nomb6=input("Ingresa tu nombre: ")

print(nomb6[0:1])


print("------------------------ejercicio 7------------------------")
nomb7=input("Ingresa tu nombre: ")

print("El último índice es: ",nomb7[-1])


print("------------------------ejercicio 8------------------------")
base8=int(input("Ingresa la base del restángulo: "))
altura8=int(input("Ingresa la base del restángulo: "))

resultado8=base8*altura8
print("El área del rectángulo es igual a: ", resultado8)


print("------------------------ejercicio 9------------------------")
año9=int(input("Ingresa tu año de nacimiento: "))
edad9=2025-año9
print("Tu edad actual es: ",edad9)


print("------------------------ejercicio 10------------------------")
nomb10=input("Ingresa un nombre de usuario: ")
domi10=input("Ingresa tu dominio: ")

print("Tu dirección de correo electrónico es: "+nomb10+"@"+domi10+".com")


print("------------------------ejercicio 11------------------------")
nomb11=input("Ingresa tu nombre: ")

print("Tu nombre tiene",len(nomb11)," letras")


print("------------------------ejercicio 12------------------------")
pala12=input("Ingresa una primer palabra: ")
palb12=input("Ingresa una segunda palabtra: ")

print(pala12+" "+palb12)


print("------------------------ejercicio 13------------------------")
pal13=input("Ingresa una palabra: ")

print("La segunda letra es: ",pal13[1:2])

print("------------------------ejercicio 14------------------------")
pal14=input("Ingresa una palabra: ")

print("Las tres primeras letras son: ¨",pal14[0:3])

print("------------------------ejercicio 15------------------------")
pal15=input("Ingresa una palabra: ")

lap15=pal15[::-1] #:: tira pa atras
print("Tu palabra invertida es: ",lap15)

print("------------------------ejercicio 16------------------------")
num116=int(input("Ingresa tu primer número: "))
num216=int(input("Ingresa tu segundo número: "))

sum16=num116+num216
res16=num116-num216
multi16=num116*num216
divi16=num116/num216

print("El resultado de su suma es: ",sum16)
print("El resultado de su resta es: ",res16)
print("El resultado de su multiplicación es: ",multi16)
print("El resultado de su division es: ",divi16)


print("------------------------ejercicio 17------------------------")
num17=int(input("Ingresa un número: "))
oper17=num17*2
print("El doble de tu número ingresado es: ",oper17)


print("------------------------ejercicio 18------------------------")
num18=int(input("Ingresa un número: "))
oper18=num18/2
print("La mitad de tu número ingresado es: ",oper18)


print("------------------------ejercicio 19------------------------")
fra19=input("Escribe una frase: ")
print("Tu frase tiene",len(fra19)," caracteres")


print("------------------------ejercicio 20------------------------")
pal20=input("Ingresa una palabra: ")
print(pal20+", "+pal20+", "+pal20)


print("------------------------ejercicio 21------------------------")
nom21= input("Ingrese su nombre: ")
print(nom21[0:2])
print (nom21[-2::])


print("------------------------ejercicio 22------------------------")
pal22= input("ingrese una palabra: ")
letra22= len (pal22)
R= letra22//2
print (pal22[R])


print("------------------------ejercicio 23------------------------")
Fra23= input("Ingresa una frase: ")
print (Fra23[0:10])


print("------------------------ejercicio 24------------------------")
num24= int(input("Ingresa un numero: "))
Res24= num24*num24

print ("Su resultado elevado al cuadrado es: ", Res24)


print("------------------------ejercicio 25------------------------")
A= int(input("Ingrese un primer numero: "))
B= int(input("Ingrese un segundo numero: "))
# Res25= (A+B+abs(A-B))//2
Res25= A*(A>=B)+B*(B>A)
print (Res25)


print("------------------------ejercicio 26------------------------")
U26= int(input("Ingrese su edad: "))
R26= U26*365
print ("Los dias que usted ha vivido son:",R26)


print("------------------------ejercicio 27------------------------")
fra26= input("Ingrese una palabra de 5 letras: ")
print (fra26[0:1])
print (fra26[1:2])
print (fra26[2:3])
print (fra26[3:4])
print (fra26[4:5])


print("------------------------ejercicio 28------------------------")
pal28= input("Ingrese una palabra: ")
# print ("Su palabra tiene mas de 5 letras: ",len (pal28)>5)
print ("Su palabra tiene menos de 5 letras: ",len (pal28)<5)


print("------------------------ejercicio 29------------------------")
p29= int(input("Ingrese un numero: "))
r= p29*10
print ("El resultado de su numero multiplicado por 10 es: ",r)


print("------------------------ejercicio 30------------------------")
pa30=input("Escribe una palabra: ")

print("Su palabra en mayúsculas es : ",pa30.upper())
print("Su palabar en minúsculas es: ",pa30.lower())
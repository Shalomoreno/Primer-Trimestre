print("-----------REGISTRO SIMPLE DE PRODUCTO Y CÁLCULO DE COSTOS-----------")
nom=input("Ingrese el nombre del producto: ")
puni=float(input("Ingrese el precio unitario del producto: "))
cant=int(input("Ingrese la cantidad de productos comprados: "))
t=(nom,puni)
lt=[t,cant]
dic={
    "producto":lt
}
print("La información de tu producto es: ", dic)
print("El costo total de tu compra es: ", lt[0][1]*lt[1])


print("-----------FACTURA DE MÚLTIPLES PRODUCTOS (versión fija sin bucles)-----------")
nom1=input("Ingrese el nombre del producto: ")
puni1=float(input("Ingrese el precio unitario del producto: ")) 
cant1=int(input("Ingrese la cantidad de productos comprados: "))

nom2=input("Ingrese el nombre del producto: ")
puni2=float(input("Ingrese el precio unitario del producto: "))
cant2=int(input("Ingrese la cantidad de productos comprados: "))

nom3=input("Ingrese el nombre del producto: ")
puni3=float(input("Ingrese el precio unitario del producto: "))
cant3=int(input("Ingrese la cantidad de productos comprados: "))

t1=(nom1,puni1)
lst1=[t1,cant1]

t2=(nom2,puni2)
lst2=[t2,cant2]

t3=(nom3,puni3)
lst3=[t3,cant3]

dic1={
    "producto1":lst1,
    "producto2":lst2,
    "producto3":lst3
}

producto1=lst1[0][1]*lst1[1]
producto2=lst2[0][1]*lst2[1]
producto3=lst3[0][1]*lst3[1]

print("Tu factura es: ", dic1)
print("El costo total de tu compra es: ", producto1+producto2+producto3)


print("-----------REGISTRO DE NOTAS DE UN ESTUDIANTES-----------")
nom2=input("Ingrese el nombre del estudiante: ")
asiga=input("Ingrese la asignatura 1: ")
asigb=input("Ingrese la asignatura 2: ")
asigc=input("Ingrese la asignatura 3: ")

nota1a=float(input("Ingrese la primera nota de la asignatura "+asiga+": "))
nota2a=float(input("Ingrese la segunda nota de la asignatura "+asiga+": "))

nota1b=float(input("Ingrese la primera nota de la asignatura "+asigb+": "))
nota2b=float(input("Ingrese la segunda nota de la asignatura "+asigb+": "))

nota1c=float(input("Ingrese la primera nota de la asignatura "+asigc+": "))
nota2c=float(input("Ingrese la segunda nota de la asignatura "+asigc+": "))

tua=(asiga,((nota1a+nota2a)/2))
tub=(asigb,((nota1b+nota2b)/2))
tuc=(asigc,((nota1c+nota2c)/2))


lsa=[tua,nota1a,nota2a]
lsb=[tub,nota1b,nota2b]
lsc=[tuc,nota1c,nota2c]

lista=[lsa,lsb,lsc]


dic2={
    "nombre":nom2,
    "materias":lista
}

prom=(tua[1]+tub[1]+tuc[1])/3

print("Tu boletín es :\n",dic2,"\nTu nota final fue de: ",prom)
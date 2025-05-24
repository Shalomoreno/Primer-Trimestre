print("Sistema de calificación:")

print("Bienvenido al sistema de calificación de notas.")
print("Por favor, a continuación, ingresa los siguientes datos:")
apellido=input("Ingresa tus apellidos: ")
nombre=input("Ingresa tu nombre: ")
grado=input("Ingresa tu grado: ")
ti=int(input("Ingresa tu documento de identidad:"))
print(f"Hola",apellido,nombre,"del grado",grado,"identificado con el número de documento",ti,",","Ingresa tus notas a continuación:")
nm=float(input("Ingresa tu nota mínima para aprobar las asignaturas: "))

print("Ingresa tus notas de matemáticas: ")
ma1=float(input("Ingresaa tu primera nota de matemáticas: "))
ma2=float(input("Ingresaa tu segunda nota de matemáticas: "))
ma3=float(input("Ingresaa tu tercera nota de matemáticas: "))
suma=ma1+ma2+ma3
proma=suma/3
print("El promedio de tu nota de matemátias es: ",proma)
print("Usted aprobó matemáticas?", proma>=nm)

print("Ahora, ingrese sus notas de español:")
es1=float(input("Ingresa tu primera nota de español: "))
es2=float(input("Ingresa tu segunda nota de español: "))
es3=float(input("Ingresa tu tercera nota de español: "))
sues=es1+es2+es3
proes=sues/3
print("El promedio de tu nota de español es: ",proes)
print("Usted aprobó matemáticas?", proes>=nm)

print("Ahora calculemos tus notas de inglés: ")
in1=float(input("Ingresa tu primera nota de inglés: "))
in2=float(input("Ingresa tu segunda nota de inglés: "))
in3=float(input("Ingresa tu tercera nota de inglés: "))
suin=in1+in2+in3
proin=suin/3
print("El promedio de tu nota de inglés es: ",proin)
print("Usted aprobó inglés?", proin>=nm)

print("Ahora calculemos tus notas de naturales: ")
na1=float(input("Ingresa tu primera nota de naturales: "))
na2=float(input("Ingresa tu segunda nota de naturales: "))
na3=float(input("Ingresa tu tercera nota de naturales: "))
suna=na1+na2+na3
prona=suna/3
print("El promedio de tu nota de naturales es: ",prona)
print("Usted aprobó naturales? ",prona>=nm)
print("Ahora calculemos tus notas de sociales:")
so1=float(input("Ingresa tu primera nota de sociales: "))
so2=float(input("Ingresa tu segunda nota de sociales: "))
so3=float(input("Ingresa tu tercera nota de sociales: "))
suso=so1+so2+so3
proso=suso/3
print("El promedio de tu nota de sociales: ",proso)
print("Usteda aprobó sociales?", proso>=nm)

print("Ahora, comprobemos si aprobó el grado:")
protsuma=proma+proes+proin+prona+proso
prototal=protsuma/5
print("El promedio de tus notas fue de: ",prototal)
print(f"El estudiante aprobó el grado? ",prototal>=nm)

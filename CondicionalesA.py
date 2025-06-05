print("-----Programa de credito bancario-----")
nom=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad en años: "))
if edad >= 18:
    print("Hola", nom, "puedes crear un credito bancario")
    print("Ingrese el siguiente dato para continuar:")
    salario=float(input("Ingresa tu salario mensual: "))
    if salario >= 1000:
        print("Tu crédito bancario ha sido aprobado")
    else:
        print("Lo sentimos, tu crédito bancario no ha sido aprobado debido a que tu salario es menor a 1000")
else:
    print("No puedes crear un credito bancario, debido a que eres menor de edad")
    

print("-----Precio para la entrada de los clientes-----")
edad=int(input("Ingrese su edad: "))
if edad < 4:
    print("La entrada es gratis\n Disfruta de tu entrada")
elif edad <= 18:
    print("El precio de la entrada es de 5 euros\n Disfruta de tu entrada")
else:
    print("El precio de la entrada es de 18 euros\n Disfruta de tu entrada")


print("-----Calculadora básica-----")
n1=float(input("Ingrese el primer número: "))
n2=float(input("Ingrese el segundo número: "))
opcion=input("Ingrese la operación que desea realizar, suma + , resta - , multiplicación * ó división /: ")
if opcion == "+":
    resultado = n1 + n2
    print("El resultado de la suma es:", resultado)
elif opcion == "-":
    resultado = n1 - n2
    print("El resultado de la resta es:", resultado)
elif opcion == "*":
    resultado = n1 * n2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == "/":
    resultado = n1 / n2
    print("El resultado de la división es:", resultado)
else:
    print("Error: No se puede dividir por cero.")
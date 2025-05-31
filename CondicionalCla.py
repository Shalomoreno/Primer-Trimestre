# edad=int(input("Ingrese su edad: "))
# if edad < 18:
#     print("Usted es menor de edad.")
# else:
#     print("Usted es mayor de edad.")

# print("----------Ejemplo 1----------")
# x=25
# if x > 10:
#     print("pon encima de diez,")
#     if x > 20:
#         print("y también por encima de 20!")
#     else:("pero no por encima de 20")
    

# print("----------Ejemplo 2----------")
# y = 15
# if y > 10:
#     print("por encima de diez")
#     if y > 20:
#         print("y también por encima de 20!")
#     else:
#         print("pero no por encima de 20")
        

print("----------Ejercicio 1----------")
a=int(input("Ingrese un primer número: "))
b=int(input("Ingrese un segundo número: "))
mul= a * b
if mul >= 1:
    print("El producto de los números es positivo")
elif mul == 0:
    print("El producto de los números es cero")
elif mul < 0:
    print("El producto de los números es negativo")
else:
    print("El producto de los números es un número no válido")

print("----------Ejercicio de mascota (diccionario)----------")

nom=input("¿Cuál es el nombre de tu mascota?: ")
tip=input("¿Cuál es la raza de "+nom+" ?: ")
edad=int(input("¿Cuál es la edad de "+nom+" ?: "))
nod=input("¿Cuál es el nombre del propietario?: ")
city=input("¿Cuál es tu ciudad natal?: ")

dic={
    "El nombre de la mascota es: ":nom,
    "La raza de "+nom+" es: ":tip,
    "La edad de "+nom+" es: ":edad,
    "El propietario es: ":nod,
    "La ciudad natal es: ":city
}

print(dic)
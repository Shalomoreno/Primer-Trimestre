print("Clientes regulares:")
clientes=["andrea", "carlos", "juan", "andres", "andrea", "felipe", "valentina", "julian", "juan", "felipe"]
print(clientes)
clientes.append("juliana") #.append utilizado para agregar elementos al final de una lista
print(clientes)
elementos=len(clientes) #len calcula la cantidad de elementos en la lista 
print(f"El número de elementos en la lista es: ", elementos)
print("El nombre mayor de la lista es: ",max(clientes)) #El mayor nombre en orden alfabético (max)
print("El nombre menor de la lista es: ",min(clientes)) #El menor nombre en orden alfabético (min)
print("El orden alfábetico de la lista es: ",sorted(clientes)) # Muestra la lista ordenada alfabéticamente 
clientes.remove("felipe") #Elimina la primera aparición de "felipe" en la lista
print(clientes)
print("El indice de JULIANA es: ",clientes.index("juliana")) #Busca el índice (posición) de "juliana" en la lista.

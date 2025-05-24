print("------------------Ejercicio 1------------------")
tupla1=(1,2,3,4,5)
print(tupla1)
print("El primer elemento de la tupla es: ",tupla1[0],"El útimo elemento de la tupla es: ",tupla1[-1]) #Se utiliza [] para la posición dentro de una tupla


print("------------------Ejercicio 2------------------")
list2=[1.1,2.2,3.3,4.4,5.5]
print(list2)
print("El segundo elemento de la lista es: ",list2[1],"El cuarto elemento de la lista es: ",list2[3])


print("------------------Ejercicio 3------------------")
tupla3=(1,2,3)
print(tupla3)
n1=tupla3[0]
n2=tupla3[1]
n3=tupla3[2] # ← Para poner en una variable el elemento de una tupla
print("Los elementos de la tupla son: ",n1,", ",n2," y ",n3)


print("------------------Ejercicio 4------------------")
list4=[1,2,3,4,5]
print(list4)
suma=list4[0]+list4[1]+list4[2]+list4[3]+list4[4] #Pone en una variable la suma de los elemntos de una tupla llamando a cada elemento según su posición
resultado=suma
print("El resultado de los elementos en la lista es: ",resultado)


print("------------------Ejercicio 5------------------")
t5=(1.1,2.2,3.3)
print(t5)
suma5=t5[0]+t5[1]+t5[2]
prom5=suma5/3
print("El promedio de la tupla es: ",prom5)


print("------------------Ejercicio 6------------------")
list6=[1,2,3,4]
print(list6)
e61=list6[0]
e62=list6[1]
e63=list6[2]
e64=list6[3]
print("Los elementos de la tupla son: ",e61,", ",e62,", ",e63," y ",e64)


print("------------------Ejercicio 7------------------")
t7=(1,2)
print(t7)
multi=t7[0]*t7[1]
print("El resultado de la multiplicación de los elementos: ",multi)


print("------------------Ejercicio 8-----------------")
list8=[3,4,5]
print(list8)
list8.append(6) #.append utilizado para agregar elementos al final de una lista, se agrega este elemento en ()
print(list8)
print("El primer elemento de la lista es: ",list8[0],"El útimo elemento de la lista es: ",list8[-1])


print("------------------Ejercicio 9-----------------")
t9=(3,5,7,9)
print(t9)
suma9=t9[0]+t9[1]
print("La suma de los dos primeros elementos de la tupla es: ",suma9)


print("------------------Ejercicio 10-----------------")
lt10=[1,2,3,4,5]
print(lt10)
resta10=lt10[1]-lt10[3]
print("La diferencia del segundo y cuarto elemento de la lista es: ",resta10)


print("------------------Ejercicio 11-----------------")
t11=(5,6,7,8,9,10)
print(t11)
multi11=t11[0]*t11[-1]
print("El resultado de la multiplicación del primer y último elemento es: ",multi11)


print("------------------Ejercicio 12-----------------")
lt12=[50,25,100]
print(lt12)
divi12=lt12[0]/lt12[-1]
print("El resultado de la división entre el primer y el tercer número es de: ", divi12)


print("------------------Ejercicio 13-----------------")
t13=(2,4,6,8)
print(t13)
print("El tercer elemento de la tupla es: ",t13[2])


print("------------------Ejercicio 14-----------------")
lt14=[0.1,0.2,0.3,0.4,0.5]
print(lt14)
suma14=lt14[0]+lt14[1]+lt14[2]+lt14[3]+lt14[4]
print("La suma de todos los elementos de la lista es de: ",suma14)


print("------------------Ejercicio 15-----------------")
lt15=[1,2,3,4]
print(lt15)
lt_a_t15=tuple(lt15) #tuple se utiliza para convertir una lista a tupla----se coloca la lista a cambiar dentro de ()
print("La lista ",lt15," conventirda en una tupla se ve: ",lt_a_t15)


print("------------------Ejercicio 16-----------------")
t16=(5,10,15,20,25)
print("La tupla es: ",t16)
t_a_lt16=list(t16) #list se utiliza para convertir una tupla a lista----se coloca la tupla a cambiar dentro de () 
print("Ahora la tupla convertida en una lista es ",t_a_lt16)
t_a_lt16.append(int(input("Agrega el siguiente multiplo de 5 a la lista: "))) #.append para agragar un valor al final
#int e input para pedir al usuario agregar el número que desee al final
print("Ahora tu lista es: ",t_a_lt16)


print("------------------Ejercicio 17-----------------")
lt17=["Banano","Papaya","Mango","Manzana","Pera"]
print("La lista es: ",lt17)
lt_a_t17=tuple(lt17)
print("Ahora la lista convertida en una tupla es : ",lt_a_t17," y su tercer elemnto es: ",lt_a_t17[2])


print("------------------Ejercicio 18-----------------")
t18=(4,9,12)
t_a_lt18=list(t18)
print("La tupla es: ",t18,"Ahora convertida en lista es: ",t_a_lt18)
nm=(int(input("¿Qué número del medio es el correcto según la secuencia? :")))
t_a_lt18[1]=nm  
#Se coloco en una variable el número cambiado por el usuario para luego reemplazar ese número en una posición determinada de la lista
print("Ahora tu lista es: ",t_a_lt18)


print("------------------Ejercicio 19-----------------")
lt19=[3,6,9,12]
lt_a_t19=tuple(lt19)
print("Ahora la lista ",lt19," convertida a tupla es: ",lt_a_t19," y la cantidad de elementos de la tupla es: ",len(lt_a_t19))


print("------------------Ejercicio 20----------------")
t20=(10,20,30,40,50)
t_a_lt20=list(t20)
print("La tupla ",t20," convertida en lista es ", t_a_lt20)
t_a_lt20.pop() #.pop elimina o devuelve un elemento según un índice (el último si no se le coloca nada)
print("Ahora tu lista removiendo el último elemento es: ",t_a_lt20)

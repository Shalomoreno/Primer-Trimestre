dictionary= {"a": 1,
             "e": 2,
             }
print ()
print (dictionary)
print (f"clave a: {dictionary['a']}")
print (f"clave e: {dictionary['e']}")

dictionary= {"numbers": [18,20,28],
             "grupos":{"a":1, "b":2}
             }
print (dictionary)
print (f"clave numbers:{dictionary['numbers']}")
print (f"clave groups: {dictionary['grupos']}")

print (f"clave numbers: {dictionary['numbers'],[1]}")
print (f"calve groups:{dictionary['grupos']['b']}")
print (dictionary,["z"])
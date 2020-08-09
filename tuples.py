x = (1, 2, 3)
print(type(x))

# Constructor
y = tuple((1, 2, 3))

print(y)

x = (1, 2, 3)
print(dir(x))

x = (1)
print(type(x))

x = (1,)

print(type(x))


x = (1,)

print(x)

x = (1,)

print(x)

#Eliminamos una tuple:

del x

# print(x) Aqui dara un error

locations = {
	(35.12312, 39.000) : "Tokyo", # => clave: latitud y longitud respectivamente
	(35.12312, 39.000) : "New York"
}

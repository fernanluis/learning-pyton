print()
dir()
type(1)
len("hello")

def hello(): # => la palabra clave def hace referencia a la definicion de una funcion.
	print("Hello World")

hello()

def hello(name):
	print("Hello " + name)

hello("joe")

def hello(name):
	print("Hello " + name)

hello("joe")
hello("ryan")
hello("luis")


def hello(name="Person"):
	print("Hello " + name)

hello()



def add(numberOne, numberTwo):
	return numberOne + numberTwo

add(10, 20) # => {esto devuelve un valor, y ese valor es: 30 pero no lo imprime

print(add(10, 20))
print(add(600, 20))

add = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(10, 30))

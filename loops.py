foods = ["apples", "bread", "cheese", "milk", "banana"]

for food in foods:
	print(foods)

for food in foods:
    if food == "cheese":
		print("You have to buy this")
print(foods)

for food in foods:
	if food == "cheese":
		break
print(foods)

for food in foods:
	if food == "cheese":
		continue # => si la condicion es True no ejecutes nada solo continua
print(foods)	   # => por eso saltea cheese en la salida correpondiente.

for number in range(1, 8):
	print(number)

for letter in "Hello": #=> palabra usada letter es arbitrario, lo cual puede ser letra,etc
	print(letter)


count = 4

while count <= 10:
	print(count)
	count = count + 1

x = 40
if  x < 30:
    print("x is less than 30") # con tabulacion

x = 10
if  x < 30:
    print("x is less than 30") # con tabulacion


x = 10
if  x < 20:
    print("x is less than 20")
else:
	print("x is greater than 20")



color = "blue"

if color == "red":
	print("the color is red")
else:
	print("any color")

color = "red"

if color == "red":
	print("the color is red")
elif color == "blue":
	print("the color is blue")
else:
	print("any color")


name = "John"
last_name = "Carter"

if name == "John":
	if last_name == "Carter":
		print("You are John Carter")
	else:
		print("You are not John")

name = "John"
last_name = "Carter"

if name == "John":
	if last_name == "Carter":
		print("You are John Carter")
	else:
		print("You are not John Carter")
else:
	print("You are not John")


if x > 2:
	if x < 100:
		print()

if x > 2 and x <= 10:
	print("x is greater than two and less than or equal to ten")
if x > 2 or x <= 20:
	print("x is greater than two and less or equal to twenty")

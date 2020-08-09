[]
demo_list = [10, "hello", 1.34, True, [1,2,3]]
colors = ["red", "green", "blue"]

#numbers_list = list(1, 2, 3, 4)
numbers_list = list((1, 2, 3, 4))
print(numbers_list)

numbers_list = list((1, 2, 3, 4))
print(type(numbers_list))

numbers_list = list((1, 2, 3, 4))

range(1,10)

r = list(range(1, 10))
print(r)

colors = ["red", "green", "blue"]

print(type(colors))

print(dir(colors))

print("green" in colors)

print("violet" in colors)

print(colors)
colors[1] = "yellow"
print(colors)


colors.append("violet")
#colors.append("violet", "yellow")
colors.append(("violet", "yellow"))
colors.append(["violet", "yellow"])
colors.extend(["violet", "yellow"])

print(colors)

colors.insert(1, "violet")
print(colors)

# colors.insert(len(colors), "violet"))

#colors.insert(len(colors), "violet"))
colors.pop()
print(colors)

colors = ["red",  "green","blue"]
colors.remove("green")
print(colors)

colors.pop(1) # => eliminar el indice 1
print(colors)

# colors = ["red",  "green","blue"]
# colors.clear()

colors = ["red",  "green","blue"]
colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

print(colors.index("red"))

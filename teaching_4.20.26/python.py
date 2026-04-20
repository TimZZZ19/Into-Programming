fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", True, 3.14]
empty = []


fruits.append("date")




# apple, banana, cherry, date
for i in range(len(fruits)): # i: 0 -> 1 -> 2 -> 3
	if fruits[i] == "cherry":
		print("Cherry found")
		break
	print(fruits[i])

print("Program finsihed")







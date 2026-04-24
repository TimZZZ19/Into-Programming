print()
# Problem 1: Random numbers and statistics

# Description:
# Generate 10 random integers between 1 and 100 (use random.randint). Then print:

# · The maximum value
# · The minimum value
# · The average (sum / count)

# import random

# # Generate 10 random integers between 1 and 100
# numbers = []
# for _ in range(10):
# 	numbers.append(random.randint(1, 100))

# # numbers = [random.randint(1, 100) for _ in range(10)]

# print("Numbers:", numbers)

# # Find max, min, sum manually with a for loop
# max_val = numbers[0]
# min_val = numbers[0]
# total = 0

# for num in numbers: ## 另一种for loop的形式，不需要知道索引，只需要知道元素本身
#     if num > max_val:
#         max_val = num
#     if num < min_val:
#         min_val = num
#     total += num

# average = total / len(numbers)

# print(f"Maximum: {max_val}")
# print(f"Minimum: {min_val}")
# print(f"Average: {average:.2f}")

# Problem 2: Count occurrences of a specific number

# Description:
# Generate 20 random integers between 1 and 10. Ask the user to enter 
# a number, then count how many times that number appears in the list. 
# Print the count.



# import random

# # Generate 20 random integers between 1 and 10
# numbers = [random.randint(1, 10) for _ in range(20)]
# print("Generated list:", numbers)

# # Ask user for a number
# target = int(input("Enter a number between 1 and 10: "))

# count = 0
# for num in numbers:
#     if num == target:
#         count += 1
# print("The number of times the input value appeared is: ", count)


# Problem 3: Frequency of all numbers (dictionary counting)

# Description:
# Generate 30 random integers between 1 and 6 (like dice rolls). 
# Using a for loop, count how many times each number appears and 
# store the counts in a dictionary. Then print the dictionary.

# scores = {
# 	"Tim":89, # key-value pair
# 	"Tom":99,
# 	"Lina":100
# }

# list = [1, 2 ,3] # list[0]
# scores["Tim"]
# socre["Tom"]


import random

# Generate 30 dice rolls
rolls = [random.randint(1, 6) for _ in range(30000)]
print("Rolls:", rolls)

# Count frequencies manually with a dictionary
freq = {}
for num in rolls:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1


# Print result
for number in sorted(freq.keys()):
    print(f"{number} appears {freq[number]} times")





print()







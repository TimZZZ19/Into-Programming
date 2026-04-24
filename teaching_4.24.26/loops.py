print()
### WHILE LOOP 的基本写法
# num = 0
# while num < 5:
# 	print(num)
# 	num += 1
# print("Program finished")	
# 
### WHILE LOOP 不受限于数字控制，其它类型的变量也行
# quit = False
# while quit == False:
# 	ans = input("Enter 1 or 0 (1:quit, 0:continue): ")
# 	if ans == "1": 
# 		quit = True
# 	else:
# 		quit = False
# 
### FOR LOOP 的基本写法，基本逻辑和用数字控制的WHILE LOOP一致
# for i in range(5): # i : 0,1,2,3,4
# 	print(i)
# print("Program finished")
# 

### BREAK
# value = 0
# while True:
#     value += 1
#     if value == 5:
#         break
#     print(value)   # prints 1,2,3,4


### WHILE LOOP 的一个基本常规应用 - LINEAR SEARCH
# list = [1,29,38,48,19,2,6]
# found = False # flag
# target = 48
# 
# # list[0]
# # list[1]
# # list[2]
# 
# for i in range(len(list)):
# 	if list[i] == target:
# 		found = True
# 		break
# 		
# if found: # !found : found == False
# 	print("Yes, found.")

# ### CONTINUE
# print("Loop 开始")
# n = 0
# while n < 5:
#     n += 1
#     if n == 3:
#         continue # skip 当前循环中的余下代码，直接到下一个循环
#     print(n)       # prints 1,2,4,5
# print("Loop 结束") 
# print()
# ### BREAK vs. CONTINUE
# print("Loop 开始")
# n = 0
# while n < 5:
#     n += 1
#     if n == 3:
#         break 
#     print(n)       # prints 1,2
# print("Loop 结束")  

### WHILE 可与 ELSE 连用
# n = 3
# if n == 1:
# 	print("quit")
# else:
# 	print("continue")
# num = 0
# while num < 3:
# 	print(num)
# 	num += 1
# else:
# 	print("Num is not smaller than 3 now.")
# 

### FUNCTIONS
# def find_target(list, target): # void 函数，即无返回值
# 	found = False # flag
# 
# 	for i in range(len(list)):
# 		if list[i] == target:
# 			found = True
# 			break
# 		
# 	if found: # !found : found == False
# 		print("Yes, found.")
# 	else:
# 		print("No, not found.")

def find_target(list, target): # return 函数，即有返回值
	found = False # flag

	for i in range(len(list)):
		if list[i] == target:
			found = True
			break
		
	if found: # !found : found == False
		return "Yes, found."
	else:
		return "No, not found."


list = [1,29,38,48,19,2,6]
target = 48
print(find_target(list, target))




print()







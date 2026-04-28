print()
### 面向对象编程

class Dog:
	# Constructor 
    def __init__(self, name, age): 
        self.__name = name   # 加上两个下划线，变成私有
        self.__age = age
        
    def bark(self):
    	print("Woof!!!")
    	
    def get_human_years(self):
    	return self.__age * 7
    	
    def get_name(self):
    	return self.__name
    	
    def get_age(self):
    	return self.__age
    
    def set_name(self, name):
    	self.__name = name
    	
    def set_age(self, age):
    	if age > 0: 
    		self.__age = age
    	else:
    		print("Age must be positive.")
    	
    	
     
# Create objects with specific data
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)
dog1.bark()
dog2.get_human_years()

print(dog1.get__name(), dog1.get__age())   # Buddy 3
print(dog2.get__name(), dog2.get__age())   # Lucy 5

print()
	

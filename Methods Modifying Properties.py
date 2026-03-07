class Person:
    def __init__(self):
        self.Name = input("Enter your name:")
        self.Age = int(input("Enter your age:"))
        
    def celebrate_birthday(self):
        self.Age += 1
        
        print("Happy birthay" , self.Name , "You are now," ,self.Age)

p1 = Person()
p1.celebrate_birthday()
     


    

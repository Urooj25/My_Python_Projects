# use of init method
class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age


    name = "Enter your name"
    age = "Enter your Age"

      p1 = Person(name,age)
    print(p1.name)
    print(p1.age)
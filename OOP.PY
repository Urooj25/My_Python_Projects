class Person:
    def __init__(self):
        self.Name = input("Enter your Name:")
        self.Class = input("Enter your Class/sec:")
        self.University = input("Enter your institution or university Name :")
        self.degree = input("What degree are you persuing:")
    def greet(self):
        print("Hello , My Name is:"+ self.Name)
        print("My section is:"+ self.Class)
        print("I am Studing in:"+ self.University)
        print("I  am persuing, "+ self.degree)
p1 = Person()
p1.greet()


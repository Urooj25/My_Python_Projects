#Methods with Parameters
class Calculator:
    def add(self):
        self.a = int(input("Enter your number 1:"))
        self.b = int(input("enter your number 2:"))
        return (self.a + self.b)

    def multiply(self):
        self.c = int(input("Enter your  number 3:"))
        self.d = int(input("enter your  number 4:"))
        return (self.c * self.d)
    def Divide(self):
        self.e = int(input("Enter your number 5 :"))
        self.f = int(input("Enter your number 6:"))
        return (self.e/self.f)
    def Subtract(self):
        self.g = int(input("Enter your number 7:"))
        self.h = int(input("Enter your number 8 "))
        return(self.g-self.h)
p1 = Calculator()

print(p1.add())
print(p1.multiply())
print(p1.Divide())
print(p1.Subtract())
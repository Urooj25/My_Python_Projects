#Methods with Parameters
class Calculator:
    def add(self):
        self.a = int(input("Enter your number 1:"))
        self.b = int(input("enter your number 2:"))
        return (self.a + self.b)

    def multiply(self):
        self.c = int(input("Enter your 3 number:"))
        self.d = int(input("enter your 4 number:"))
        return (self.c * self.d)
p1 = Calculator()

print(p1.add())
print(p1.multiply())

class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_addition(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")

obj1 = Expression(10, 20, 30)
obj1.calculate_addition()

obj2 = Expression(5, 15, 25)
obj2.calculate_addition()
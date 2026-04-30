class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

rect = Rectangle(10, 5)
print(f"Rectangle Area: {rect.get_area()}") 

sq = Square(4)
print(f"Square Area: {sq.get_area()}")       
print(f"Square Perimeter: {sq.get_perimeter()}") 
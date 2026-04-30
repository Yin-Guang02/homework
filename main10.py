class Rectangle:
    """Parent class representing a general rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates area: length * width."""
        return self.length * self.width

    def perimeter(self):
        """Calculates perimeter: 2 * (length + width)."""
        return 2 * (self.length + self.width)

class Square(Rectangle):
    """Sub-class representing a square, inheriting from Rectangle."""
    def __init__(self, side):
        super().__init__(side, side)

# --- Example Usage ---
my_rect = Rectangle(10, 5)
print(f"Rectangle Area: {my_rect.area()}")        

my_square = Square(4)
print(f"Square Area: {my_square.area()}")            
print(f"Square Perimeter: {my_square.perimeter()}")  
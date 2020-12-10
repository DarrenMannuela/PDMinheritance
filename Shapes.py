import math


class Shape:
    def __init__(self, color="red", filled=True):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color: str):
        self.color = color

    def is_filled(self):
        return self.filled

    def set_filled(self, filled: bool):
        self.filled = filled

    def to_string(self):
        return f"\nThe color is: {self.color}\nIs it filled: {self.filled}"


class Circle(Shape):

    def __init__(self, radius=1.0):
        super().__init__()
        self.radius = radius
        self.area = 0
        self.perimeter = 0

    def get_radius(self):
        return self.radius

    def set_radius(self, radius: float):
        self.radius = radius

    def get_area(self):
        self.area = math.pi**self.radius
        return self.area

    def get_perimeter(self):
        self.perimeter = math.pi*(2*self.radius)
        return self.perimeter

    def to_string(self):
        self.get_area()
        self.get_perimeter()
        return f"\nThe radius of the Circle: {self.radius}" \
               f"\nThe area of the Circle: {self.area}\nThe perimeter of the Circle: {self.perimeter}"


class Rectangle(Shape):
    def __init__(self, width=1.0, length=1.0):
        super().__init__()
        self.width = width
        self.length = length
        self.area = 0
        self.perimeter = 0

    def get_width(self):
        return self.width

    def set_width(self, width: float):
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length: float):
        self.length = length

    def get_area(self):
        self.area = self.length*self.width
        return self.area

    def get_perimeter(self):
        self.perimeter = 2*self.length+2*self.width
        return self.perimeter

    def to_string(self):
        self.get_area()
        self.get_perimeter()
        return f"\nThe width of the Rectangle: {self.width}\nThe length of the Rectangle: {self.length}" \
               f"\nThe area of the Rectangle: {self.area}\nThe perimeter of the Rectangle: {self.perimeter}"


class Square(Rectangle):
    def __init__(self):
        super().__init__()
        self.area = 0
        self.perimeter = 0

    def get_side(self):
        return self.length

    def set_side(self, side: float):
        self.set_width(side)
        self.set_length(side)

    def to_string(self):
        self.get_area()
        self.get_perimeter()
        return f"\nThe width of the Square: {self.width}\nThe length of the Square: {self.length}" \
               f"\nThe area of the Square: {self.area}\nThe perimeter of the Square: {self.perimeter}"
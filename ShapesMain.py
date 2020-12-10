from Shapes import Circle
from Shapes import Square
from Shapes import Rectangle


def main():
    print("\nWelcome to Basic Geometry calculator:")
    print("\nWhat is the shape:\n1.Circle\n2.Rectangle\n3.Square")
    pick = int(input("\nWhat is your choice(1-3):"))
    if pick == 1:
        radius = input("What is its radius:")
        radius = float(radius)
        circle = Circle()
        circle.set_radius(radius)
        print(circle.to_string())

    elif pick == 2:
        length = input("What is its length:")
        width = input("What is its width:")
        length, width = float(length), float(width)
        rectangle = Rectangle()
        rectangle.set_length(length)
        rectangle.set_width(width)
        print(rectangle.to_string())

    elif pick == 3:
        side = input("What is its side:")
        side = float(side)
        square = Square()
        square.set_side(side)
        print(square.to_string())

    else:
        print("Invalid option")
        pass


if __name__ == "__main__":
    while True:
        main()

class Rectangle:
    # Initialize the Rectangle class with width and height attributes
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # String representation of the Rectangle object
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # Method to set the width of the rectangle
    def set_width(self, width):
        self.width = width

    # Method to set the height of the rectangle
    def set_height(self, height):
        self.height = height

    # Method to calculate the area of the rectangle
    def get_area(self):
        return self.width * self.height

    # Method to calculate the perimeter of the rectangle
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Method to calculate the diagonal of the rectangle using the Pythagorean theorem
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Method to generate a string representation of the rectangle using '*' characters
    # Returns a message if the rectangle is too large
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    # Method to calculate how many times another shape can fit inside the rectangle
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    # Initialize the Square class with equal width and height (side length)
    def __init__(self, side):
        super().__init__(side, side)

    # String representation of the Square object
    def __str__(self):
        return f"Square(side={self.width})"

    # Method to set the side length of the square
    def set_side(self, side):
        self.width = side
        self.height = side

    # Override the set_width method to set both width and height to the same value
    def set_width(self, width):
        self.set_side(width)

    # Override the set_height method to set both width and height to the same value
    def set_height(self, height):
        self.set_side(height)

class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return (("*" * self.width) + "\n") * self.height

    def get_amount_inside(self, shape):
        num_wide = self.width // shape.width
        num_tall = self.height // shape.height

        return num_wide * num_tall

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def set_side(self, side):
        super().set_width(width=side)
        super().set_height(height=side)

    def set_width(self, width):
        self.set_side(side=width)

    def set_height(self, height):
        self.set_side(side=height)

    def __str__(self):
        return f"Square(side={self.width})"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):  # noqa: WPS615
        self.width = width

    def set_height(self, height):  # noqa: WPS615
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50:
            return "Too big for picture."

        string_rect = ""

        for _ in range(self.height):  # noqa: WPS
            string_rect += "*" * self.width + "\n"

        return string_rect

    def get_amount_inside(self, fitting_shape):
        fitting_shape_area = fitting_shape.width * fitting_shape.height
        current_shape_area = self.width * self.height

        return int(current_shape_area / fitting_shape_area)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_width(self, width):  # noqa: WPS615
        self.width = width
        self.height = width

    def set_height(self, height):  # noqa: WPS615
        self.width = height
        self.height = height

    def set_side(self, length):  # noqa: WPS615
        self.width = length
        self.height = length

    def __str__(self):
        return f"Square(side={self.width})"

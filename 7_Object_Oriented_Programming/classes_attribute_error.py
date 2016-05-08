# Trying to access an attribute of an instance that isn't defined causes an 'AttributeError'.
# This also applies when you call an undefined method.
#
# Example:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(7, 8)
print(rect.color)

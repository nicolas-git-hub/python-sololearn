# Classes can have other 'methods' defined to add functionality to them.
# Remember, that all methods must have 'self' as their first parameter.
#
# These methods are accessed using the same 'dot' syntax as attributes.
#
# Example:

print()

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('Woof!')

fido = Dog('Fido', 'brown')
print(fido.name)
fido.bark()


#
# Classes can also have 'classes attributes', created by assigning variables within the body of the class.
# These can be accessed either from instances of the class, or the class itself.

print()

class AnotherDog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = AnotherDog('Fido', 'brown')
print(fido.legs)
print(AnotherDog.legs)


# Class attributes are shared by all instances of the class.

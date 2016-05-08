# A class that inherits from another class is called a subclass.
# A class that is inherited from is called a superclass.
# If a class inherits from another with the same attributes or methods, it overrides them.

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('Grr...')

class Dog(Wolf):
    def bark(self):
        print('Woff!')

husky = Dog('Max', 'grey')
husky2 = Wolf('Max2', 'gray')

husky.bark()
print()
print(husky2.name)
print(husky2.color)
husky2.bark()

#
# In the example above, 'Wolf' is the superclass, 'Dog' is the subclass.

# We have previously loked at two paradigms of programming:
#
# - imperative: using statements, loops, and functions as subroutines
# - functional: using pure functions, higher-order functions, and recursion.
#
# Another very popular paradigm is object-oriented programming (OOP).
#
# Objects are created using classes, which are actually the focal of OOP.
# The class describes what the object will be, but is separate from the object itself.
# In other words, a class can be described as an object's blueprint, description, or definition.
#
# You can use the same class as a blueprint for creating multiple different objects.
#
#
# Classes are created using the keyword 'class' and an indented block, which contains
# class methods (which are functions).
#
# Below is an example of a simple class and its objects.

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat('ginger', 4)
rover = Cat('dog-coloured', 4)
stumpy = Cat('brown', 3)

# This code defines a class named 'Cat' which has two attributes: 'color' and 'legs'.
#
# Then the class is used to create 3 separate objects of that clas.
#
# ==============================================================================
#
# The __init__ method is the most important method in a class.
# This is called when an instance (object) fo the class is created, using the class name as a function.
#
# All methods must have 'self' as their first parameter, although it isn't explicitly passed,
# Python adds the 'self'argument to the list for you; you do not need to include it when you
# call the methods.
#
# Within a method definition, 'self' refers to the instance calling the method.
#
# Instances of a class have 'attributes', which are pieces of data associated with them.
# in this example, 'Cat' instances have attributes 'color' and 'legs'.
# These can be accessed by putting a dot, and the attribute name after an instance.
#
# In an '__init__' method, self.attribute can therefore be used to set the initial value
# of an instance'a attribute.
#
# Example:

print(felix.color)

#
# In the example above, the '__init__' method takes two arguments and assigns them to the
# object's attributes. The '__init__' method is called the class constructor.

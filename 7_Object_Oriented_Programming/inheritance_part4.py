# The function "super " is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's superclass.
#
# Example:

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

# super().spam() calls the spam method of the superclass.

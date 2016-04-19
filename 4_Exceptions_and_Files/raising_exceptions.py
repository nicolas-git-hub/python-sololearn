# Raising Exceptions
#
# You can raise exceptions by using the raise statement.

print(1)
#raise ValueError <- had to be commented.
print(2)

# You need to specify the type of the exception raised.

# Exceptions can be raised with arguments that give detail about them.

name = "123"
#raise NameError("Invalid name!") <- had to be commented.

#
# In except blocks, the raise statement can be used without arguments
# to re-raise whatever exception occoured.

try:
    num = 5 / 0
except:
    print("An error accoured")
    raise

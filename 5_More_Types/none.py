# The "None" object is used to represent the absence of a value.
# It is similar to null in other programming languages.
# Like other "empty" values, such as (), [] and the empty string,
# it is "False" when converted to a "Boolean variable".
# When entered at the Python console, it is displayed as the empty string.

print(None == None)

print(bool(None) == bool(()))
print(bool(None) == bool([]))
print(bool(None) == bool(""))
print(bool(None) == False)

# Output: True

# Considerations:
# None is an absence of a value
# None object is returned by any function that doesn't return anything else
#
# Consider:

def some_func():
    print("Hi")

var = some_func()
print(var)

# This outputs "Hi" and "None"

# ==============================

# Another example:

foo = print()
if foo == None:
    print(1)
else:
    print(2)

# It outputs "1" because function print() returns None

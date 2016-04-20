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

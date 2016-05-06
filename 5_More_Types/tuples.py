# Tuples are very similar to list execpt that they are immutable (they cannot be changed).
# Also, they are created using parenthesis rether than square brackets.
#
# Like lists and dictionaries, tuples can be nested within each other.
#
# Example:

words = ('spam', 'eggs', 'sausages',)

# You can access the values in the tuple with their index, just as you do with lists.

print(words)
print(type(words))
print(words[0])


# Trying to reassign a value in a tuple causes a TypeError.

# words[1] = 'cheese' # <--- This line had to be commented in order the script to reach the end

# Tuples can be created without the parenthesis, by just separating the values with commas.
#
# Example:

my_tuple = 'one', 'two', 'three'
print(my_tuple[0])
print(type(my_tuple))

# An empty tuple is created using an empty parenthesis pair

tpl = ()
print(tpl)
# print(tpl[0]) # <--- Causes index error because tuple is empty
print(type(tpl))

# Tuples are faster than lists, but they cannot be changed.

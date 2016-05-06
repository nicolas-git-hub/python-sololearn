# List comprehensions are a useful way of quickly creating lists
# whose contents obey a simple rule.
#
# List comprehensions are inpired by set-builder notation in mathematics.
#
# Example:

cubes = [i**3 for i in range(5)]
print(cubes)

#
# A list comprehension can also contain an if statement to enforce a condition
# on values in the list.
#
# Example:

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print('\n')
print(evens)


# Trying to create a list in a very extensive range will result in a MemoryError.
# This code shows an example where the list comprehension runs out of memory.

# even = [2*i for i in range(10**100)]
# print('\n')
# print(even)
#
# From my experience, it actully didn't display an error message but it freezed the system.
#
# This issue is solved by generators, which are covered in the next module.

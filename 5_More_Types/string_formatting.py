# So far, to combine strings and non-strings, we've coverted the non-strings to strings and added them.
# String formating provides a more powerful way to embed non-strings within strings.
# String formating uses a string's format method to substitute a number of arguments in the string.
#
# Example:

nums = [4, 5, 6]
msg = 'Numbers: {0} {1} {2}'.format(nums[0], nums[1], nums[2])
print(msg)


# Each argument of the format function is placed in the string at the correspondent position,
# which is determined using the curly braces {}.
#
# Another example:
# What is the result of this code?

print('\n')
print('{0}{1}{0}'.format('abra', 'cad'))

#
# String formating can also be done with named arguments.
#
# Example:

a = '{x}, {y}'.format(x = 5, y = 12)
print('\n')
print(a)

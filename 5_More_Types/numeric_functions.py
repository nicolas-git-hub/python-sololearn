# To find the maximum or minimum of some numbers or a list, you can use max ou min.
# To find the distance of a number from zero (its absolute value), use abs.
# To round a number to a certain number os decimal places, use round.
# To find the total of a list, use sum.
#
# Some examples:

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

#
# Another example:
#
# What is the result of this code?

a = min([sum([11, 22]), max(abs(-30), 2)])
print('\n')
print(a)


# Often used in conditional statements, 'all' and 'any' take a list as an argument, and
# return True if all or any (respectively) of their arguments evaluate to True (and False
# otherwise).
# The function enumerate can be used to iterate through the values and indices of a list
# simultaneously.
#
# Example:

print('\n')
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print('All larger than 5.')

if any([i % 2 == 0 for i in nums]):
    print('At least one is even')

for v in enumerate(nums):
    print(v)


print('\n')

for v in enumerate(nums):
    v = str(v)
    v = v.replace('(', 'Index: ')
    v = v.replace(', ', '  Value: ')
    v = v.replace(')', '')
    print(v)

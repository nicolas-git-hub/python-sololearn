# The module itertools is a standard library that contains several functions that
# are useful in functional programming.
# One type of functions it produces is infinite iterators.
#
# The function count counts up indefinitely from a value.
# The function cycle indefitely iterates through an iterable (for instance a list or string).
# The function repeat repeats an object, either indefinitely or a specific number of times.

try:
    from itertools import count
except:
    print('Error while importing')


for i in count(3):
    print(i)
    if i >= 11:
        break


#
# There are many functions in itertools that operate on iterables, in a similar way to map and filter.
#
# Some Examples:
#
# takewhile - takes items from an iterable while a predicate function remains true;
# chain - combines several iterables into one long one.
# accumulate - returns a running total of values in an iterable.

try:
    from itertools import accumulate, takewhile
except:
    print('Error while importing')

print()

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))


#
# There are also several combinatoric functions in itertools, such as product and permutation.
# these are used when you want to accomplish a task with all possible combinations os some items.
#
# Example:

try:
    from itertools import product, permutations
except:
    print('Error while importing')

print()

letters = ('A','B')
print(list(product(letters, range(2))))
print(list(permutations(letters)))

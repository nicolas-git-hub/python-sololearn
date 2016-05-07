# Sets are data structures, similar to lists or dictionaries.
# They are created using curly braces, or the se function.
# They share some functionality with lists, such as the use of 'in' to check whether they contain
# a particular item.

num_set = {1, 2, 3, 4, 5}
word_set = set(['spam', 'eggs', 'sausages'])

print(3 in num_set)
print('spam' not in word_set)

# To create an empty set, you must use set() as {} creates an empty dictionary.

#
# Sets differ from lists in several ways, but share several list operations such as 'len'.
# They are unordered, which means that they can't be indexed.
# They cannot contain duplicates elements.
#
# Due to the way they're stored, it's faster to check whether an item is part of a set, rather
# than part of a list.
#
# Instead of using append to add to a set, use add.
#
# The method remove removes a specific element from a set, pop removes an arbitrary element.

print()

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
nums.pop()
print(nums)


# Basic uses of sets include membership testing and the elimination of duplicate entries.

#
# Sets can be combined using mathematical operations.
# The union operator | combines two sets to from a new one containing items in either.
# The intersection operator & sets items only in both.
# The difference operator - gets items in the first set but not in the second.
# The symmetric difference operator ^ gets items in either set, but not both.

print()

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

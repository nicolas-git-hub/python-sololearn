"""
Another way of alternating lists is using the "append" method.
This adds an item to the end of an existing list.
"""

nums = [1, 2, 3]
nums.append(4)
print(nums)

# The dot before the "append" shows it is a method of the list class.

words = ["hello"]
words.append("world")
print(words[1])
print(type(words))
print(type(words[1]))
words.append(123)
print(type(words))
print(type(words[2]))
print(words)

# To print the lenght of a 

nums = [1, 3, 5, 2, 4]
print(len(nums))

# "len" is a function and not a method.

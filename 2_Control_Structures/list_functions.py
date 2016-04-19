# Another way of alternating lists is using the "append" method.
# This adds an item to the end of an existing list.


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

# "len" is a function and not a method. No dot as in "append".

#The insert method is similar to append, except that it allows you
# to insert a new item at an position in the list, as opposed to just
# at the end

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)


nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(nums)
print(len(nums))

# The "index" method finds the first occurence
# of a list and returns its index.
# If the item isn't in the list, it raises a ValueError.

letters =["p", "q", "r", "s", "p", "u"]
print(letters.index("r"))
print(letters.index("p"))
print(letters.index("z"))

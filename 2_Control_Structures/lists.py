# Lists are another type of object in Python
# They store an indexed list of items
# Lists are created using the square brackets and commas
# To access an certain item of a list, use its index in the squere brackets

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

# Lists can be empty

empty_list = []
print(empty_list)

# Typically, a list will contain itens of a single item type but it can 
# store several types. List can also be nested within other lists.

number = 3
things = ["stings", 0, [1, 2, number], 4.56]
print(things[0])
print(things[1])
print(things[2])
print(things[2][2])
print(things[3])

print("\n")
num = [5, 4, 3, [2], 1]
print(num[3])
print(num[3][0])

# Strings can be indexed. Integers, can't be

string = "Hello World!"
print(string[6])

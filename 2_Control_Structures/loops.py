"""
Sometimes, you need to perform code on each item on a list.
This is called iteration, and it can be accomplished with a "while"
loop and a counter variable.
"""

words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
    word = words[counter]
    print(word + "!")
    counter = counter + 1

"""
The example above iterates through all itens in list, accesses them using
their indices, and prints them with exclmation marks.


Python also provides a "for" loop.
The same code can be written with a for loop.
"""

print("\n")
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

"""
The "for" loop is commonly used to repeat some code a certain number of times.
This is done by combining "for" loops with range objects.
"""

print("\n")
for i in range(5):
    print("hello!")

"""
Example: Fill the blanks to create a "for" loop that prints only the
even values in the range.
"""

print("\n")
for i in range(0, 20, 2):
    print(i)

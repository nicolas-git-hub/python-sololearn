# The content of a file that has been opened in text mode can be read
# using the read method

file = open("files/lorem_ipsum.txt", "r")
content = file.read()
print(content)
print("Total number of characters: " + str(len(content)))
file.close()

# This will print all the content of the file "files/lorem_ipsum.txt"
# and display its number of characters

#
# To read only a certain amount of a file, you can provide a number as
# an argument to the read function.
#
# This determines the number of bytes that should be read.
#
# You can make more calls to read on the same file object to read more
# of the file byte by byte.
#
# With no argument, read returns the rest of the file.

print("\n")

file = open("files/lorem_ipsum.txt", "r")
print("0 - " + file.read(100) + "\n")
print("1 - " + file.read(100) + "\n")
print("2 - " + file.read(100) + "\n")
print("3 - " + file.read(100) + "\n")
print("4 - " + file.read())
file.close()

# Same idea as above but with a different code

print("\n")

# It opens and reads a file to count its length, to make some math
# and to store it on variables

file = open("files/lorem_ipsum.txt", "r")
file_read = file.read()

# Here you define how many characters of the file are going to appear
# on each line
characters_per_line = 80

floor_division = len(file_read) // characters_per_line
division_remainder = len(file_read) % characters_per_line

file.close() # It closes file to make its content it available again

# Here it opens the file again to grab the content later
file = open("files/lorem_ipsum.txt", "r")

# Now it writes the lines
i = 0
for i in range(floor_division):
    print(str(i) + " - " + file.read(characters_per_line) + "\n")
    
if division_remainder != 0:
    print (str(i + 1) + " - " + file.read(division_remainder))

file.close()

#
# As we just saw, after all contents in a file have been read, any
# attempts to read futher from that that file will return an empty
# string, because you are trying to read from the end of the file.

print("\n")

file = open("files/lorem_ipsum.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

#
# Retriving lines of a text file
#
# To retrive lines in a file, you can use the "readlines" function
# to return a list in which each element is a line in the file

file = open("files/countries.txt", "r")
print(file.readlines())
file.close()

#
# You can also use a for loop to iterate through the lines in the file:

file = open("files/countries.txt", "r")
for line in file:
    print(line)

file.close()

# In the output, the lines are separated by blank lines, as the print
# function automatically adds a new line at the end of its output

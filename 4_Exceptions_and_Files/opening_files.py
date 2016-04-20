# You can use Python to read and write the content of files.
# Text files are the easiest to manipulate.
# Before a file can be edited, it must be opened, using the open function.

my_file1	= open("filename.txt")

# The argument of the open function is the path to the file.
# If the file is in the same directory as the program, you can specify
# only its name.

# You can specify the mode used to open a file by aplying a second
# argument to the open function.
#
# Sending "r" means open in read mode, which is the default mode.
# Sending "w" means write, for rewriting the contents of a file.
# Sending "a" means apend mode, for adding new content to the end of the file.
# 
# Adding "b" to a mode opens it in binary mode, which is used for
# non-text fles (such) as image and sound files).


print("\n")

# read mode
open("filename.txt")
open("filename.txt", "r")

# write mode
open("files/lorem_ipsum.txt", "w")

# binary write mode
open("filename.txt", "wb")

#
# Closing a file
# Once a file has been opened and used, you should close it.
# This is done with the "close" method of the file object.

file = open("filename.txt", "w")
# do stuff to the file
file.close()

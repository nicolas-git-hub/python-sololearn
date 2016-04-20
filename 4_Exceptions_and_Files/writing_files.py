# Writing files
#
# To write files you use the write method which writes a sting to the file

file = open("files/newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("files/newfile.txt", "r")
print(file.read())
file.close()

# The w creates the file if it doesn't exist.

# When a file is opened in write mode, the file's existing content
# is deleted

print("\n")

# First we open a file which already has some initial content 
file = open("files/newfile1.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

# Then we open it in write mode and insert some new content
file = open("files/newfile1.txt", "w")
file.write("Some new text")
file.close()

print("------------------------")

# Then we open the same file again in read mode to check the content
file = open("files/newfile1.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

# As we could see, the initial content has been overwritten by the
# string in write mode.


# ------------------------------------------------------------------

# The write method returns the number of bytes written to a file,
# if successful

msg = "Hello World!"
file = open("files/newfile2.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

# Therefore file.write(msg) == len(msg)

# ------------------------------------------------------------------

# It's a good practice to avoid wasting resources by making sure that
# files are always closed after they have been used. One way of doing
# this is to use "try" and "finally".

try:
    f = open("files/lorem_ipsum.txt", "r")
    print(f.read())
finally:
    f.close()

# This ensures that the file is always closed, even if an error occurs.

# -------------------------------------------------------------------

# Working with files
#
# An alternative way of doing this is using "with" statement.
# This creates a temporary variable (often called "f"), which is only
# accessible in the indented block of the "with" statement.

with open("files/newfile2.txt", "r") as f:
    print(f.read())

# The file is automatically closed at the end of the "with" statement,
# even if exceptions occur within it.

# This is an example project, showing a program that analyzes a sample file to find
# the percentage of the text each character occupies.
#
# This section shows how a file could be open and read.

filename = input('Enter a filename:')
# Suggestion: files/lorem_ipsum.tct

with open(filename) as f:
    text = f.read()

print(text)

#
# This part of the program shows a function that counts how many times a character occurs in a string.

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

#
# This function takes as its arguments the text of the file and one character, returning the number
# of times that character appears in the text.
#
# Now, we can call it for our file.

for char in 'abcdefghijklmnopqrstuvwxyz':
    perc = 100 * count_char(text, char) / len(text) 
    print('{0} - {1}%'.format(char, round(perc, 2)))

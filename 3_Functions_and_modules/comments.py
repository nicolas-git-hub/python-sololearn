"""
Comments are annotations to code used to make easier to understand.
They don't affect how code is run.
In Python, a comment is created y inserting an octothorpe (#).
All the text after it on that line is ignored
"""

x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment


"""
Docstrings:

Docstrings (documentation strings) serve a similar purpose to comments,
as they are designed to explain code. However, they are more specific
and have a different syntax.
They are created by putting a multiline string containing an explanation
of the function below the function's name first line.
"""

def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

shout("spam")

"""
Unlike conventional comments, docstrings are
retained thoughout the runtime of the program.
This allows the programmer to inspect these
comments at run time.
"""

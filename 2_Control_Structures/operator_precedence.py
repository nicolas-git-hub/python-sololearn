"""
Operator precedence is a very important concept in programming.
It's an extension of the mathematical idea of order of operations
(multiplication being performed before addition, etc)...

Python's order of operators is the same as that of normal mathematics:
1 - Parenthesis
2 - Exponentioation
3 - Multiplication / Division
4 - Addition / Subtraction
"""

print(False == False or True)
print(False == (False or True))
print((False == False) or True)

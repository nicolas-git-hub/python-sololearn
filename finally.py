# finaly
#
# To ensure some code runs no matter what erros occour, you can use a
# "finally" statement. The "finally" statement is placed at the bottom
# of a try/except statement. Code within a finally statement always runs
# after execution of the code in the try, and possibily in the except,
# blocks.

try:
    print("Hello.")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero.")
finally:
    print("This code runs no matter what.")

# Code in a "finally" statement even runs if an uncaught exception
# occours in one of the preceding blocks.

print("\n")
try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed fast")

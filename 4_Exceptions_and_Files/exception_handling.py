# Exception Handling
#
# An exception statement without any exception specified will catch all
# erros. These should be used sparingly, as they can catch unexpected
# erros and hide programming mistakes.

try:
    word = "spam"
    print(word / 0)
except:
    print("An error occourred.")

# Exception handling is particularly useful when dealing with user input.

try:
    num1 = input("Number1: ")
    num2 = input("Number2: ")
    print(float(num1)/float(num2))
except:
    print("Invalid input.")

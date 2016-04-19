# Range: the range function creates a sequential list of numbers (integers)

numbers = list(range(10))
print(numbers)

# If "range" is called with one argument, it produces an object with 
# values from 0 to that argument (as the above example)
# 
# If it called with rwo arguments, it produces values from first to the
# second.

print("\n")
numbers = list(range(3, 8))
print(numbers)


print("\n")
print(range(20) == range(0, 20))

# range can have a third argument, which determines the interval of the
# sequence produced. This third argument must be an integer.

print("\n")
numbers = list(range(5, 20, 2))
print(numbers)
print(len(numbers))

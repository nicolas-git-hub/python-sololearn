# Lists: an item of an list can be reassigned.

nums = [7, 7, 7, 7, 7]
nums[2] = 5

print(nums)


# Lists can be added and multiplied in the same way as strings

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

"""
List Operations

To check if an item is in a list, the "in" operator can be used.
It returns "True"if the item occurs one or more times in the list,
and "False" if it doesn't.\
"""

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

"""
To check if an item in not in a list, you can use the "not" operator
in the following ways:
"""

nums = [1, 2, 3]
print("\n")
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

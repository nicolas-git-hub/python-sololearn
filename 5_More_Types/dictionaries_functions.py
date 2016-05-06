# Just like lists, dictionary keys can be assigned to different values.
# However, unlike lists, a new dictionary key can also be assigned a
# value, not just ones that already exist.

squares ={1: 1, 2: 4, 3: 'error', 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)
print('============================\n')

# ====================================================================

# To determine whether a key is in a dictionary, you can use 'in' and
# 'not in', just as you can for a list.

nums = {
    1: 'one',
    2: 'two',
    3: 'three',
}

print(nums)
print(1 in nums)
print('three' in nums)
print(4 not in nums)
print('============================\n')


# A useful dictionary method is 'get'. It does the same thing as indexing, 
# but if the key is not found in the dictionary, it returns another
# specified velue instead ('None', by default)

pairs = {1: 'apple',
    'orange': [2, 3, 4],
    True: False,
    None: 'True',
}

print(pairs.get('orange'))
print(pairs.get(7))
print(pairs.get(12345, 'not in dictionary'))
print('==============================\n')

# Example
#
# What is the result of this code?

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

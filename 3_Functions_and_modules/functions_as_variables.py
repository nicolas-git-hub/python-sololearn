# Although they are created differently from normal variables,
# functions are just like any other kind of value.
# They can be assigned and reassigned to variables,
# and later referenced by those names.

def multiply(x, y):
    return x * y

a = 4
b = 7

operation = multiply

print(operation(a, b))

# The example above assigned the function multiply to
# a variable operation. Now, the name operation can also
# be used to call the function.

# Python contains many useful built-in functions and methods to accomplish commom tasks.
#
#
# join - joins a list of strings with another string as separator.
#
# replace - replaces one substring in a string with another.
#
# startswith and endswith - determine if there is a substring at the start and end of a string, respectively
#
# lower and upper - to change the case of a string
#
# method split - does the opposite of join; turning a string with a certain separator into a list.
#
#
# Some examples:

print(', '.join(['spam', 'eggs', 'ham']))

print('\n')
print('Hello PLANET'.replace('PLANET', 'World!'))

print('\n')
print('This is a sentence.'.startswith('This'))

print('\n')
print('This is another sentence.'.endswith('sentence.'))

print('\n')
print('This is a third sentence.'.upper())

print('\n')
print('This is the last sentence.'.lower())

print('\n')
print('spam, eggs, ham'.split(', '))

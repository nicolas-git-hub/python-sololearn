# Python uses intentation for if statements (no {})

if 10 > 5:
	print("10 is greater than 5")
	
print("Program ended")


# Nested if

num = 12
if num > 5:
	print("Bigger than 5")
	if num <= 47:
		print("Between 5 and 47")


num = 48
if num > 5:
	print("Bigger than 5")
	if num <= 47:
		print("Between 5 and 47")

# Else statements

x = 4
if x == 5:
	print("Yes")
else:
	print("No")


# If, else chain

num = 5
if num == 5:
    print("Number is 5")
else:
    if num == 11:
        print("Number is 11")
    else:
        if num == 7:
            print("Number is 7")
        else:
            print("Number isn't 5, 11 or 7")

# Elif statement (shortcut for "else if")

num = 6
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")

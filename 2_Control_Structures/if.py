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

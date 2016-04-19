# An if statement runs once.
# A while statement can run more than once.
# The statements inside it are repeatedely executed as long as the condition holds.
# Once it evaluates to False, the next session of the code is executed.

i = 1
while i <= 5:
    print(i)
    i = i + 1

print("Finished")

i = 9999
while i >= 0:
    print(str(i) + " - in the loop")
    i = i - 1

# While with "break". Using "break" outside the loop causes an error.

i = 0
while 1 == 1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

# The "continue" statement don't break the loop, it just skips it

i = 0
while True:
    i = i + 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished")

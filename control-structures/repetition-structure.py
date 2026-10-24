# repetition structures are otherwise known as LOOPS
# they allow us to execute a block of code multiple times
# Python primarily supports two types of loops: for loops (Count-controlled loops) and while loops (Condition-controlled loops).

# FOR LOOPS: using range() function
# The range() function generates a sequence of numbers, which can be used to control the number of iterations in a for loop. 
# The range() function can take one, two, or three arguments: start, stop, and step.
# The start argument specifies the starting value of the sequence (inclusive), the stop argument specifies the ending value of 
# the sequence (exclusive), and the step argument specifies the increment between each value in the sequence. 
# If only one argument is provided, it is treated as the stop value, and the start value defaults to 0. 
# If two arguments are provided, they are treated as the start and stop values, and the step value defaults to 1. 
# If three arguments are provided, they are treated as the start, stop, and step values.

range(1,3) # generates a sequence of numbers from 1 to 2 (exclusive of 3)
range(5) # generates a sequence of numbers from 0 to 4 (exclusive of 5)
range(1, 10, 2) # generates a sequence of numbers from 1 to 9 (exclusive of 10) with a step of 2

for num in range(6): # loop will iterate 5 times (0 to 5)
    # print(num + " * " + num + " = " + (num * num))
    print(f'{num} * {num} = {num * num}')

for x in range(1, 6):
    print('hi', x)

for y in range(1, 10, 2):
    print("Holla", y)

for m in range(1, 5):
    print("*" * m)
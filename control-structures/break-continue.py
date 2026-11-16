# BREAK and CONTINUE STATEMENTS
# break: Terminates the loop prematurely and jumps to the next statement outside the loop.
# continue: Skips the remaining code in the current iteration and jumps to the next cycle.

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# print even numbers
# method 1
for i in range(1, 20):
    if(i % 2 != 0):
        continue
    print(i)

# method 2
for i in range(1, 1001):
    if(i % 2 == 0):
        print(i)
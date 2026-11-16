val = input('Enter a value: ')
a = int(val)
val = input('Enter a value: ')
b = int(val)

result = 1;
for i in range(1, b):
    result = result * a

print(f"The result of {a} raised to the power of {b} is: {result} {a ** b}")
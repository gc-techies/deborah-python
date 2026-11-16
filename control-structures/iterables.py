# ITERATION OR ITERATE

# Iterables are objects that can be looped over. In Python, common iterables include lists, tuples, strings, 
# dictionaries, and sets. You can use a for loop to iterate over these iterables.

# example one: range() function generates a sequence of numbers, which are iterable.

# example two: strings are iterable, and you can loop through each character in a string.
for s in 'Deborah':
    print(f'Character: {s}')

# example three: lists are iterable, and you can loop through each element in a list.
# when creating a list, you can use square brackets [] and separate the elements with commas.
num_list = [1, 2, 3, 4, 5]
str_list = ['apple', 'banana', 'cherry']

for num in num_list:
    print(f'Number: {num}')

for fruit in str_list:
    print(f'Fruit: {fruit}')
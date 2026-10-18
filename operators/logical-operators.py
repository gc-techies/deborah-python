# logical operators are used to combine conditional statements. The logical operators are: and, or, not
print(f"True and True: {True and True}")  # True
print(f"True and False: {True and False}")  # False
print(f"False and False: {False and False}")  # False
print(f"True or True: {True or True}")  # True
print(f"True or False: {True or False}")  # True
print(f"False or False: {False or False}")  # False
print(f"not True: {not True}")  # False
print(f"not False: {not False}")  # True

age = 19
cash = 500
print(f"Can purchase item: {age >= 18 and cash >= 500}")
print(f"Can purchase item: {age >= 18 or cash >= 500}")
# other programming languages
ageCap = age >= 18 and age <= 65
print(f"Age is between 18 and 65: {ageCap}")  # Checks if age is between 18 and 65 (inclusive)
# Python allows for a more concise way to check if a value is within a range using chained comparisons:
print(f"Age is between 18 and 65: {18 <= age <= 65}")  # Checks if age is between 18 and 65 (inclusive)
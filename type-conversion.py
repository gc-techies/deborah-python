val = input('Enter a value: ')
print(f"The data type of the value you entered is: {type(val)}")
print(f"The value you entered is: {val}")
concat = val + '10'
print(f"The concat of the value you entered and 10 is: {concat}")
# sum = int(val) + 10
# print(f"The sum of the value you entered and 10 is: {sum}")
print(f"{bool(int(val))} is the boolean value of the value you entered, {bool(0)}")

# int() conversion
# float() conversion
# bool() conversion
# str() conversion

# FALSY VALUES: 
# '' => empty string
# 0 => zero
# None => NoneType

# TRUTHY VALUES:
# '0' => string with zero
# and anything not in the falsy values list is considered truthy. For example, 'False' is a string and is considered truthy. 

# Operators, operands
fname = ' Deborah is in the house '
lname = "Ogunsaju"
letter = """
This is a multi-line string. It can span multiple lines and is often used for "documentation" or long text blocks.
just testing out having a multi-line string in python.
"""

print(fname + " " + lname)  # Concatenation of strings
print('Deborah' + ' ' + 'Ogunsaju')  # Concatenation of strings
print(letter)  # Printing the multi-line string
length = len(fname)  # Getting the length of the first name
print(length)  # Printing the length of the first name
print(fname[0])  # Printing the first character of the first name
print(fname[0:3])  # Printing the first three characters of the first name
print(fname[-1])  # Printing the last character of the first name
print(fname[:5])  # Printing the first five characters of the first name
print(fname[5:])  # Printing the characters of the first name from index 5 to the end
print(fname[:])
print(fname[5:0])

# FORMATTED STRINGS
concat = "hello, my name is " + fname + " " + lname + " and I am a software engineer."
print(concat)
formattedStr = f"hello, my name is {fname} {lname} and I am a software engineer. {2 + 2} is equal to {len(letter)}."
print(formattedStr)

upper = letter.upper()  # Converts the string to uppercase
print(upper)  # Printing the uppercase string
lower = letter.lower()  # Converts the string to lowercase
print(lower)  # Printing the lowercase string
fname_stripped = fname.lstrip()  # Removes any leading whitespace from the string
print(fname_stripped)  # Printing the string with leading whitespace removed

fname_rstripped = fname.rstrip()  # Removes any trailing whitespace from the string
print(fname_rstripped)  # Printing the string with trailing whitespace removed

fname_stripped = fname.strip()  # Removes any leading and trailing whitespace from the string
print(fname_stripped)  # Printing the string with leading and trailing whitespace removed

letter.find("multi-line")  # Finds the index of the first occurrence of the substring "multi-line" in the string
print(letter.find("multi-line", 20))  # Printing the index of the first occurrence of the substring

letter.replace("multi-line", "single-line")  # Replaces all occurrences of the substring "multi-line" with "single-line" in the string
print(letter.replace("multi-line", "single-line"))  # Printing the string with the substring

lname.startswith("BO")  # Checks if the string starts with the substring "O"
print(lname.startswith("BO"))  # Printing the result of the check
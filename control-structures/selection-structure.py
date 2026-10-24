# selection statements include if, if-else, and if-elif-else statements, match-case. 
# These statements allow you to control the flow of your program based on certain conditions.
hour = 22
if hour < 12:
    print("Good morning!")
    print("Have a great day!")
elif hour < 18:
    print("Good afternoon!")
    print("Have a great day!")
elif hour < 21:
    print("Good evening!")
    print("Have a great evening!")
else:
    print("Good night!")
    print("Have a great night!")

age = 17
cash = 400
student = True
if age >= 18 and cash >= 500:
    print("You can purchase the item with AND.")
else: 
    print("You cannot purchase the item with AND.")

if age >= 18 or cash >= 500:
    print("You can purchase the item with OR.")
else: 
    print("You cannot purchase the item with OR.")

# Either age is 18 and above or Cash >= 500 and student is True
if (age >= 18 or cash >= 500) and student:
    print("You can purchase the item with OR and AND.")
else: 
    print("You cannot purchase the item with OR and AND.")

# switch-case statement in Python is implemented using the match-case statement. 
# It allows you to match a value against multiple patterns and execute different blocks of code based on the 
# matched pattern.

status_code = 403
match status_code:
    case 200:
        print("Request successful.")
        print("The request was successful and the server returned the requested data.")
    case 404:
        print("Resource not found.")
        print("The requested resource could not be found.")
    case 500:
        print("Internal server error.")
        print("An internal server error occurred.")
    case _: # default case
        print("Unknown status code.")
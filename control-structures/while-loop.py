number = 100
while number > 0:
    print(number)
    number *= 2


command = ''
while command.lower() != 'exit':
    command = input('Enter a command (type "exit" to quit): ')
    print(f'You entered: {command}')
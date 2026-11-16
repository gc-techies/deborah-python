# Outter loop iterates over x from 0 to 4
for x in range(5):
    # Inner loop iterates over y from 0 to 4
    for y in range(5):
        print(f'({x}, {y})')
    print('end of inner loop, starting next outer loop cycle')  # Move to the next line after inner loop completes
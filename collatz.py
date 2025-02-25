import sys

result = 0 # Results variable to store current iteration and loop sequence over

def collatz(number):
    global result
    if number % 2 == 0: # If number is even
        result = number // 2

    else: # If number is odd
        result = 3 * number + 1

    print(result)

print('Enter a number:')

while True: # Main loop for input
    try:
        collatz(int(input()))

        while result != 1: # Collatz Sequence loop, reiterating over result
           collatz(result)

        if result == 1:
           sys.exit()

    except ValueError: # Error handling input
        print('You must input an integer number')
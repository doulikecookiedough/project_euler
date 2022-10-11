# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def get_multiple(val1, val2):
    counter = 1
    sum = 0

    while counter < 1000:
        quotient_one = counter % val1
        quotient_two = counter % val2
        if quotient_one == 0 or quotient_two == 0:
            sum = sum + counter
        counter = counter + 1

    return sum


result = get_multiple(3, 5)
print(result)

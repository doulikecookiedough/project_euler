# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def get_largest_prime_factor(num):
    # Prime numbers can be only divisible by itself and 1
    # Find all the numbers that can be divisible from the input number
    # Determine if the numbers are prime numbers
    # Create a new list
    # Select the last item in the list (largest prime factor)

    num_factor_list = []
    for i in range(1, num + 1):
        # i is divisibe if there is no remainder
        if num % i == 0:
            # print(f"divisible: {i}")
            num_factor_list.append(i)

    prime_factor_list = []
    for n in num_factor_list:
        print(n)


if __name__ == '__main__':
    get_largest_prime_factor(60)
    # get_largest_prime_factor(13195)
    # get_largest_prime_factor(600851475143)

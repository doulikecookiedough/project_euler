# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def get_largest_prime_factor(num):
    # Prime numbers can be only divisible by itself and 1
    # Find all the numbers that can be divisible from the input number
    # Determine if the numbers are prime numbers
    # Create a new list
    # Select the last item in the list (largest prime factor)

    # num_factor_list = []
    # for i in range(1, num + 1):
    #     # i is divisibe if there is no remainder
    #     if num % i == 0:
    #         # print(f"divisible: {i}")
    #         num_factor_list.append(i)

    prime_factor_list = []
    for i in range(1, num + 1):
        if i != 1 and num % i == 0:
            prime_number_flag = 0
            for j in range(1, i):
                if i % j == 0:
                    if prime_number_flag >= 2:
                        pass
                    else:
                        prime_number_flag += 1

            if prime_number_flag >= 2:
                prime_number_flag = 0
                pass
            else:
                prime_factor_list.append(i)
                prime_number_flag = 0

    print(prime_factor_list)


if __name__ == '__main__':
    # get_largest_prime_factor(60)
    get_largest_prime_factor(13195)
    # get_largest_prime_factor(600851475143)

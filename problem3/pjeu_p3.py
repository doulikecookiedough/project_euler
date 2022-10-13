# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


# Loses effectiveness as N grows larger
def get_largest_prime_factor_sol_1(num):
    largest_prime_factor = 1
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
                if i > largest_prime_factor:
                    largest_prime_factor = i
                prime_number_flag = 0

    return largest_prime_factor


def get_largest_prime_factor_sol_2(num):
    # Determine new algorithm to quickly generate a list of prime numbers equal to provided number
    print(num)


if __name__ == '__main__':
    # result = get_largest_prime_factor(60)
    # result = get_largest_prime_factor_sol_1(13195)
    result = get_largest_prime_factor_sol_2(13195)
    # result = get_largest_prime_factor(600851475143)
    print(result)

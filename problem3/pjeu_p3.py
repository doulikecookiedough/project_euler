# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import math

# Loses effectiveness as N grows larger
# Not a good solution


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


# Still loses effectiveness as N grows larger
# Try again...
def get_largest_prime_factor_sol_2(num):
    def check_for_remainder(num, val):
        modulo_check = num % val
        if modulo_check == 0:
            return True
        else:
            return False

    def is_prime_number(num):
        prime_number_flag = 0
        for i in range(1, num):
            if num != 1 and num % i == 0:
                prime_number_flag += 1
            if prime_number_flag >= 2:
                return False
        return True

    # Get first divisible factor
    start_value = 2
    largest_divisible_factor = 0

    while largest_divisible_factor == 0:
        status = check_for_remainder(num, start_value)
        if status == True:
            largest_divisible_factor = int(num / start_value)
        else:
            start_value += 1
            check_for_remainder(num, start_value)

    prime_factor_list = []
    for p in range(start_value, largest_divisible_factor):
        if num % p == 0:
            prime_status = is_prime_number(p)
            if prime_status == True:
                prime_factor_list.append(p)

    return prime_factor_list[-1]


def get_largest_prime_factor_sol_3(num):
    # Create a prime factor tree
    # Get the first two factors, then break it down from there
    # Add all the numbers to a list, sort the list

    def check_for_remainder(num, val):
        modulo_check = num % val
        if modulo_check == 0:
            return True
        else:
            return False

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(num):
        first_factor = 2
        second_factor = 0

        factor_list = []

        # Begin the process by getting first two factors
        while second_factor == 0:
            status = check_for_remainder(num, first_factor)
            if status == True:
                second_factor = int(num / first_factor)
                factor_list.append(first_factor)
                factor_list.append(second_factor)
            else:
                first_factor += 1
                check_for_remainder(num, first_factor)

        # Now get the rest...

        return factor_list

    factor_list = get_factors(num)
    return factor_list


if __name__ == '__main__':
    # result = get_largest_prime_factor(60)
    # result = get_largest_prime_factor_sol_1(13195)
    result = get_largest_prime_factor_sol_3(600851475143)
    # result = get_largest_prime_factor(600851475143)
    print(result)

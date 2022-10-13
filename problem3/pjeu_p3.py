# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import math


def get_largest_prime_factor_sol_1(num):
    """Loses effectiveness as N grows larger, not an efficient solution"""
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
            else:
                if i > largest_prime_factor:
                    largest_prime_factor = i
                prime_number_flag = 0

    return largest_prime_factor


def get_largest_prime_factor_sol_2(num):
    """Still loses effectiveness as N grows larger, try again..."""
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
        if status is True:
            largest_divisible_factor = int(num / start_value)
        else:
            start_value += 1
            check_for_remainder(num, start_value)

    prime_factor_list = []
    for dnum in range(start_value, largest_divisible_factor):
        if num % dnum == 0:
            prime_status = is_prime_number(dnum)
            if prime_status is True:
                prime_factor_list.append(dnum)

    return prime_factor_list[-1]


def get_largest_prime_factor_sol_3(num):
    """Use the concept of a factor tree to improve performance"""

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
        second_factor = num

        factor_list = []
        # Start the process, determine if the provided number is a prime number
        factor_flag = is_prime(second_factor)

        # While the number to check is not a prime number, continue to retrieve factors
        while factor_flag is False:
            modulo_status = check_for_remainder(second_factor, first_factor)
            if modulo_status is True:
                # If the second factor is divisible by the first, add the two factors to the array
                second_factor = int(second_factor / first_factor)
                factor_list.append(first_factor)
                factor_list.append(second_factor)
                # Then reset the process
                factor_flag = is_prime(second_factor)
                first_factor = 2
            else:
                # If the second factor is not divisible by the first factor, increment the first factor until it is
                first_factor += 1
                check_for_remainder(num, first_factor)

        # Once we have the factor list, iterate over it and determine the largest prime factor
        largest_prime_factor = 0
        for factor in factor_list:
            prime_status = is_prime(factor)
            if prime_status:
                if factor > largest_prime_factor:
                    largest_prime_factor = factor

        return largest_prime_factor

    factor_list = get_factors(num)
    return factor_list


if __name__ == '__main__':
    # result = get_largest_prime_factor(60)
    # result = get_largest_prime_factor_sol_1(13195)
    result = get_largest_prime_factor_sol_3(600851475143)
    print(result)

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
    largest_prime_factor = 0

    while largest_divisible_factor == 0:
        status = check_for_remainder(num, start_value)
        if status == True:
            largest_divisible_factor = int(num / start_value)
            first_divisible_factor = start_value
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
    # Review prime factor tree
    print(num)


if __name__ == '__main__':
    # result = get_largest_prime_factor(60)
    # result = get_largest_prime_factor_sol_1(13195)
    result = get_largest_prime_factor_sol_2(13195)
    # result = get_largest_prime_factor(600851475143)
    print(result)

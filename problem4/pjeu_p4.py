# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def get_largest_product_two_digit_palindrome():
    """Testing two digits to confirm initial ideas."""
    product = 91 * 99
    result = str(product)
    if result[0] == result[3]:
        first_digit = result[0]
        last_digit = result[3]
        print("True")
        print(f"first_digit: {first_digit}")
        print(f"second_digit: {last_digit}")
    if result[1] == result[2]:
        second_digit = result[1]
        third_digit = result[2]
        print("True")
        print(f"second_digit: {second_digit}")
        print(f"third_digit: {third_digit}")
    return result


def get_largest_product_three_digit_palindrome(num):
    """This is not a working solution. Largest palindrome not found."""
    def get_product(val1, val2):
        product = val1 * val2
        return product

    def determine_palindrome(number):
        check_value = str(number)
        start = 0
        end = len(check_value) - 1
        palindrome_status = 0

        while end >= 3:
            if check_value[start] == check_value[end]:
                end -= 1
                start += 1
                palindrome_status += 1
            else:
                return False

        # print(f"palindrome_status: {palindrome_status}")
        if palindrome_status == 3:
            return True
        else:
            return False

    num_length = len(str(num))
    check_palindrome = False
    val1 = num
    val2 = num

    switch_flag = True
    while check_palindrome is False and len(str(val1)) == num_length and len(str(val2)) == num_length:
        print(val1, val2)
        check_number = get_product(val1, val2)
        check_palindrome = determine_palindrome(check_number)
        # Decrease numbers based on a switch flag
        if switch_flag is False:
            switch_flag = True
        else:
            switch_flag = False
        # If it's palindrome, end the check
        if check_palindrome:
            break
        else:
            # Decrease numbers and check again
            if switch_flag is False:
                val2 -= 1
            else:
                val1 -= 1

    return check_number


def get_largest_product_three_digit_palindrome_2(num):
    def get_product(val1, val2):
        product = val1 * val2
        return product

    def determine_palindrome(number):
        check_value = str(number)
        start = 0
        end = len(check_value) - 1
        palindrome_status = 0

        while end >= 3:
            if check_value[start] == check_value[end]:
                end -= 1
                start += 1
                palindrome_status += 1
            else:
                return False

        # print(f"palindrome_status: {palindrome_status}")
        if palindrome_status == 3:
            return True
        else:
            return False

    def get_palindrome_status(val1, val2):
        check_number = get_product(val1, val2)
        palindrome_status = determine_palindrome(check_number)
        if palindrome_status:
            return check_number
        else:
            return False

    largest_palindrome = 0

    for i in range(num, 100, -1):
        for j in range(i, 100, -1):
            check_number = get_palindrome_status(i, j)
            if check_number is not False:
                if check_number > largest_palindrome:
                    largest_palindrome = check_number

    return largest_palindrome


if __name__ == '__main__':
    # result = get_largest_product_two_digit_palindrome()
    start_number = 999
    # result = get_largest_product_three_digit_palindrome(start_number)
    result = get_largest_product_three_digit_palindrome_2(start_number)
    print(result)

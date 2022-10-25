# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def get_largest_product_two_digit_palindrome():
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


def get_largest_product_three_digit_palindrome():
    first_number = 999
    second_number = 999


if __name__ == '__main__':
    # result = get_largest_product_two_digit_palindrome()
    result = get_largest_product_three_digit_palindrome()
    print(result)

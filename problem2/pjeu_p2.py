# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def get_fibonacci_even_valued_sum(num):
    fibonacci_array = []

    a = 0
    b = 1
    c = a + b

    while c < num:
        if len(fibonacci_array) < 1:
            fibonacci_array.append(c)
        a = b
        b = c
        c = a + b
        fibonacci_array.append(c)

    even_valued_sum = 0

    for term in fibonacci_array:
        if term % 2 == 0:
            even_valued_sum += term

    return even_valued_sum


if __name__ == '__main__':
    result = get_fibonacci_even_valued_sum(4000000)
    print(result)
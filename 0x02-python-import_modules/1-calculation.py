#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, product, and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    sum_result = add(a, b)
    diff_result = sub(a, b)
    product_result = mul(a, b)

    try:
        quotient_result = div(a, b)
        print("{} + {} = {}".format(a, b, sum_result))
        print("{} - {} = {}".format(a, b, diff_result))
        print("{} * {} = {}".format(a, b, product_result))
        print("{} / {} = {}".format(a, b, quotient_result))
    except ZeroDivisionError:
        print("Cannot divide by zero.")

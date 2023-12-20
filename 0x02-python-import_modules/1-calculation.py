#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, product, and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    num1 = 10
    num2 = 5

    sum_result = add(num1, num2)
    diff_result = sub(num1, num2)
    product_result = mul(num1, num2)

    try:
        quotient_result = div(num1, num2)
        print("{} + {} = {}".format(num1, num2, sum_result))
        print("{} - {} = {}".format(num1, num2, diff_result))
        print("{} * {} = {}".format(num1, num2, product_result))
        print("{} / {} = {}".format(num1, num2, quotient_result))
    except ZeroDivisionError:
        print("Cannot divide by zero.")

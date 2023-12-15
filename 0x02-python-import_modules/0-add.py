#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of 1 and 2 using the add function."""
    from add_0 import add

    m = 1
    n = 2
    sum_result = add(m, n)

    print("{} + {} = {}".format(m, n, sum_result))

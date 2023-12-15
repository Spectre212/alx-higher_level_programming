#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of all command-line arguments."""
    import sys

    total_sum = sum(int(arg) for arg in sys.argv[1:])
    print("{}".format(total_sum))

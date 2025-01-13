#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the given number. If n is 0, returns 1.

    Description:
        The function uses recursion to calculate the factorial of the input number.
        The base case is factorial(0) = 1. For other cases, it returns n * factorial(n-1).
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

# Main execution
if __name__ == "__main__":
    # Compute the factorial of the input number from the command-line arguments
    f = factorial(int(sys.argv[1]))
    print(f)  # Print the result
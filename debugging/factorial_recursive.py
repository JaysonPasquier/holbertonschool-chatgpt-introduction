#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given number. If n is 0, returns 1.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call for factorial(n-1)

# Main script execution
if __name__ == "__main__":
    # Ensure an argument is passed to the script
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative-integer>")
        sys.exit(1)

    try:
        # Convert the command-line argument to an integer
        num = int(sys.argv[1])

        # Validate that the number is non-negative
        if num < 0:
            print("Error: Please provide a non-negative integer.")
            sys.exit(1)

        # Compute and print the factorial
        result = factorial(num)
        print(result)

    except ValueError:
        # Handle cases where the input cannot be converted to an integer
        print("Error: Please provide a valid integer.")
        sys.exit(1)
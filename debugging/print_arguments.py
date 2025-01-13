#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
else:
    print("No arguments were provided.")

#!/usr/bin/python3

def uppercase(str):
    # Loop through each character
    for char in str:
        # Convert to uppercase if needed
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end='')  # Print uppercase letter
        else:
            print("{}".format(char), end='')  # Print non-lowercase character

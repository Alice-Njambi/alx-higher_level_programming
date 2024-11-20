#!/usr/bin/python3

def uppercase(str):
    # Loop through each character
    for char in str:
        # Convert to uppercase if needed
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end='')  # Print uppercase letter
        else:
            print(char, end='')  # Print non-lowercase character.

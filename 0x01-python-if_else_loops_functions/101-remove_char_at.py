#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str  # Return the original string if the index is out of range

    # Create a new string with the character at position n removed
    return str[:n] + str[n+1:]  # Concatenate the parts before and after 

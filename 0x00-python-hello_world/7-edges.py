#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]       # Slicing to get the first 3 letters
word_last_2 = word[-2:]       # Slicing to get the last 2 letters
middle_word = word[1:-1]      # The word without the first and last letters
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")

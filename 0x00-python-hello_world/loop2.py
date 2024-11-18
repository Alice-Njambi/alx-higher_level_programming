#!/usr/bin/python3

def main ():
    
    #program to calculate the product of input numbers by user.

    n = int(input("How many numbers will you calculate the product? "))
    sum = 0

    for i in range(n):
        number = int(input("Enter number to be calculated: "))
        sum = number + sum

        print(f"Sum of numbers = {sum}")
main ()

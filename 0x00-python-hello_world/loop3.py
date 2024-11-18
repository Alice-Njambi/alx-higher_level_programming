#!/usr/bin/python3

def main ():
    #Program to calculate using while loop.
    n = int(input("Enter number of numbers to calculate product: "))
    product = 1
    i=0
    while (i<n):
        number = int(input("Enter number to calc: "))
        product =  product * number
        i += 1
    print(f"Product of numbers = {product}")
main()

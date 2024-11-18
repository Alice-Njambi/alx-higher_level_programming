#!/usr/bin/python3

def main():
    n = int(input("How many numbers do you have? "))
    total = 0.0
    for i in range(n):
        x = float(input("Enter a number >> "))
        total = total + x
        average = total/n
        print("\nThe average of the numbers is {}\n".format(average))
main() 

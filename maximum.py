#!/usr/bin/env python3
#
# Created by Marcus A. Mosley
# Created on November 2020
# This program finds the largest number of a random array of 10 numbers

import random


def max_number(number_array):
    # This function finds the largest number of a random array of 10 numbers

    largest_number = number_array[0]

    for i in number_array:
        if i > largest_number:
            largest_number = i

    return largest_number


def main():
    # This function gets input

    number_array = []

    # Input
    for loop_counter in range(0, 10):
        number = random.randint(1, 100)
        number_array.append(number)
        print("The random number is: {}".format(number))
    print(" ")

    # Call Functions
    largest_number = max_number(number_array)

    print("The largest number is {}".format(largest_number))


if __name__ == "__main__":
    main()

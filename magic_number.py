#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# RNG number guessing game without crash

import random


def main():
    # This function sees if the user inputed the magic number

    print("Guess the magic number (0-9)!")

    # Input
    magic_number_string = input("Please enter your guess: ")

    # Process
    try:
        magic_number = int(magic_number_string)

        random_number = random.randint(0, 9)

        if magic_number == random_number:
            # Output
            print("Nice! Your answer is right!")
        else:
            # Output
            print("Oops! Your answer is wrong!")
            print("The correct answer was: {}".format(random_number))

    except Exception:
        print("This isn't an integer")


if __name__ == "__main__":
    main()

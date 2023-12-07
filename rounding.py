#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 7th, 2023
# This program asks the user for a number
# and a number of decimal places
# it then rounds that number and displays it
# with the proper amount of decimal places


def round_decimal(dec_num_float, num_places):
    # Round number to correct amount of decimal places
    dec_num_float[0] = dec_num_float[0] * (10 ** num_places[0])
    dec_num_float[0] = dec_num_float[0] + 0.5
    dec_num_int = int(dec_num_float[0])
    dec_num_float[0] = dec_num_int / (10 ** num_places[0])


def main():
    # Passing by reference
    num_float = []
    num_places_int = []

    # get number and number of decimal places from user
    num_str = input("Enter a number: ")
    num_places_str = input("Enter the number of decimal places: ")

    # Check if input is valid
    try:
        num_float.append(float(num_str))
        try:
            num_places_int.append(int(num_places_str))

            # If number of places is negative
            if num_places_int[0] < 0:
                print("{} is not a valid number of places.".format(num_places_int[0]))
            else:
                # Call function to round number
                round_decimal(num_float, num_places_int)

                # Display rounded number
                print(
                    "{} rounded to {} decimal places is {}".format(
                        num_str, num_places_int[0], num_float[0]
                    )
                )
        except:
            # number of places is not an integer
            print("{} is not an integer.".format(num_places_str))
    except:
        # number is not a float
        print("{} is not a float.".format(num_str))


if __name__ == "__main__":
    main()

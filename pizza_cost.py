#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the price of a pizza
#     with inputted diameter


import constants


def main():
    # I calculate circumference

    # input
    diameter = int(input("Enter the diameter of the pizza you would like in inches: "))

    # process
    sub_total = constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()

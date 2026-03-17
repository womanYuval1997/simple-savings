"""Toy simple-interest calculator: python3 app.py 1000 5 2"""
import argparse
import math


def balance(principal, annual_percent, years):
    values = (principal, annual_percent, years)
    if not all(math.isfinite(value) and value >= 0 for value in values):
        raise ValueError("Enter finite, nonnegative values")
    return principal * (1 + annual_percent / 100 * years)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("principal", type=float)
    parser.add_argument("annual_percent", type=float)
    parser.add_argument("years", type=float)
    args = parser.parse_args()
    try:
        print(f"Final balance: {balance(args.principal, args.annual_percent, args.years):.2f}")
    except ValueError as error:
        parser.error(str(error))

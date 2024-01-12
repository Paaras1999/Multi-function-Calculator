from fractions import Fraction
import math

def solve_proportion(a, b, c, x):
    # Solves the proportion a:b = c:x
    return (b * c) / a

def solve_equation(equation):
    # Solves for x in the equation
    # Assuming the equation is in the form ax + b = 0
    a, b = equation.split('x')
    a, b = float(a), float(b)
    return -b / a

def factor_square_root(number):
    # Factors the square root of a number
    root = math.isqrt(number)
    return root

def decimal_to_fraction(decimal):
    # Converts a decimal to fraction
    return Fraction(decimal).limit_denominator()

def decimal_to_percent(decimal):
    # Converts a decimal to percent
    return decimal * 100

def fraction_to_decimal(fraction):
    # Converts a fraction to decimal
    return float(fraction)

def fraction_to_percent(fraction):
    # Converts a fraction to percent
    return float(fraction) * 100

def percent_to_decimal(percent):
    # Converts a percent to decimal
    return percent / 100

def percent_to_fraction(percent):
    # Converts a percent to fraction
    return Fraction(percent / 100).limit_denominator()


print("1. Solve Proportion: ", solve_proportion(2, 4, 6, 0))
print("2. Solve Equation: ", solve_equation("2x+4"))
print("3. Factor Square Root: ", factor_square_root(25))
print("4. Decimal to Fraction: ", decimal_to_fraction(0.75))
print("5. Decimal to Percent: ", decimal_to_percent(0.75))
print("6. Fraction to Decimal: ", fraction_to_decimal(Fraction(3, 4)))
print("7. Fraction to Percent: ", fraction_to_percent(Fraction(3, 4)))
print("8. Percent to Decimal: ", percent_to_decimal(50))
print("9. Percent to Fraction: ", percent_to_fraction(50))
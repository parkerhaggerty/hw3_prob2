# Author: Parker Haggerty
# Date: 2/14/17
# Assignment 3, Problem 2

from math import sqrt
import cmath

# Variables
a = float(input("Please enter coefficient a: \n"))
b = float(input("Please enter coefficient b: \n"))
c = float(input("Please enter coefficient c: \n"))

# Primary Equations
x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)

# Second form of Equation
x_alt1 = (2*c)/(-b+(sqrt((b**2)-(4*a*c))))
x_alt2 = (2*c)/(-b-(sqrt((b**2)-(4*a*c))))

# Final form of Equation (uses complex math sqrt)
my_x1 = (-b + cmath.sqrt((b**2)-(4*a*c)))/(2*a)
my_x2 = (-b - cmath.sqrt((b**2)-(4*a*c)))/(2*a)

# Output
print("x1:", x1)
print("x2:", x2)
print("x_alt1:", x_alt1)
print("x_alt2:", x_alt2)
print("my_x1:", my_x1)
print("my_x2:", my_x2)


# Results for a=0.001, b=1000, c=0.001

# Part A: 
# x1: -9.999894245993346e-07
# x2: -999999.999999

# Part B:
# x_alt1: -1000010.5755125057
# x_alt2: -1.000000000001e-06

# Part C:
# my_x1: (-9.999894245993346e-07+0j)
# my_x2: (-999999.999999+0j)

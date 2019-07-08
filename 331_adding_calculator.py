"""Make a calculator that allows a user to add, subtract, multiply and divide
   integers. This must only be done by addition, eg the user enters 4*3, but
   the program must work this out by addition. User may only enter ints, 
   and the results can only be ints
https://www.reddit.com/r/dailyprogrammer/comments/6ze9z0/20170911_challenge_331_easy_the_adding_calculator/
"""

# Add y to x
def addition(x, y):
    result = x + y
    return result

# Subtract y from x
# currently taking y from x, not going negative
def subtract(x, y):
    difference = 0
    while x < y:
        difference = difference + 1
        x = x + 1
    return difference


# multiply x y times
def multiply(x, y):
    result = 0
    if y == 0:
        result = 0
        return result
    for i in range(y):
        result = result + x
    return result

#divide x by y
def divide(x, y):
    if y == 0
       cant divide by 0

# x to the y
def exponent(x, y):
    # do multiply(x, x) y times?
    result = 0
    if y == 0:
        result = 1
        return result
    for i in range(y):
        result = multiply(x, x)
    return result

#put in "main" block
# check if answer is int
if not ininstance(<var>, int):
    return non-int

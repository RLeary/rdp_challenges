"""

https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

calculate the additive persistence of a number, defined as how many loops you have to do summing its digits until you get a single digit number. Take an integer N:

Add its digits

Repeat until the result has 1 digit

The total number of iterations is the additive persistence of N.

Your challenge today is to implement a function that calculates the additive persistence of a number.

Examples
13 -> 1
1234 -> 2
9876 -> 2
199 -> 3

"""

def add_persistance(number, persistance = 0):
    if number < 10:
        return persistance
    result = 0
    while number:
        result = result + number % 10
        number = number // 10
    return add_persistance(result, persistance + 1)


print(add_persistance(13))
print(add_persistance(1234))
print(add_persistance(9876))
print(add_persistance(199))
print(add_persistance(19999999999999999999999))

    

"""
def additive_persistance(number):
    result = sum(int(digit) for digit in str(number))
    persistance = 0
    if result < 10:
        persistance = persistance + 1
        return persistance
    else:
        persistance = persistance + 1
        return additive_persistance(result)

print(additive_persistance(199))
"""
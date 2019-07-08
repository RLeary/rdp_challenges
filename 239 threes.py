"""
https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

Enter a number

If the number is divisible by 3, divide it by 3.

If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.

Stop when you reach "1".

"""

# add some validation
number = int(input("Enter an integer: "))

while number > 1:
    if number % 3 == 0:
        print("%d 0" %number)
    elif number % 3 == 1:
        number = number - 1
        print("%d -1" %number)
    elif number % 3 == 2:
        number = number + 1
        print("%d 1" %number)
    number = number / 3
print('1')
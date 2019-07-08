"""
https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
Your input will contain one or more lines, where each line will be in the form 
of "NdM"; for example:

3d6
4d12
1d10
5d4


You should output the sum of all the rolls of that specified die, each on their 
own line. so if your input is "3d6", the output should look something like

14
Just a single number, you rolled 3 6-sided dice, and they added up to 14.

Bonus
In addition to the sum of all dice rolls for your output, print out the result 
of each roll on the same line, using a format that looks something like

14: 6 3 5
22: 10 7 1 4
9: 9
11: 3 2 2 1 3

Challenge Input
5d12
6d4
1d2
1d8
3d6
4d20
100d100
"""

import random

# Roll a single dice
def roll(sides):
    result = random.randint(1, sides)
    return result

# print(roll(40))

while True:
    dice = input().split('d')
    rolls = []
    for x in range(int(dice[0])):
        rolls.append(roll(int(dice[1])))
    # List comprehenion instead of for loop
    # rolls = [random.randint(1, int(dice[1])) for rolls in range(int(dice[0]))]
    print(sum(rolls),": ", rolls)
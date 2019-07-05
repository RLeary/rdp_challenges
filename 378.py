"""
https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/
It was a dark and stormy night. Detective Havel and Detective Hakimi arrived at
the scene of the crime. Other than the detectives, there were 10 people present. 
They asked the first person, "out of the 9 other people here, how many had you 
already met before tonight?" The person answered "5". They asked the same 
question of the second person, who answered "3". And so on. The 10 answers 
they got from the 10 people were:
5 3 0 2 6 2 0 7 2 5
The detectives looked at the answers carefully and deduced that there was an 
inconsistency, and that somebody must be lying. (For the purpose of this 
challenge, assume that nobody makes mistakes or forgets, and if X has met Y, 
that means Y has also met X.)

Your challenge for today is, given a sequence of answers to the question "how 
many of the others had you met before tonight?", apply the Havel-Hakimi 
algorithm to determine whether or not it's possible that everyone was telling the truth.
"""

""" Warm up 1: given a sequence of numbers, return the same set of numbers 
    with all the 0's removed
""" 

def warmup1(numbers):
    non_zero_numbers = []
    for item in numbers:
        if item > 0:
            non_zero_numbers.append(item)
    return non_zero_numbers

"""
print("warm up 1: remove 0's")
>>>print("warmup1([5, 3, 0, 2, 6, 2, 7, 2, 5]): ", warmup1([5, 3, 0, 2, 6, 2, 7, 2, 5]))
warmup1([5, 3, 0, 2, 6, 2, 7, 2, 5]): [5, 3, 2, 6, 2, 7, 2, 5]
>>>print("warmup1([4, 0, 0, 1, 3]): ", warmup1([4, 0, 0, 1, 3]))
print("warmup1([4, 0, 0, 1, 3]): [4, 1, 3]
>>>print("warmup1([0, 0, 0]): ", warmup1([0, 0, 0]))
warmup1([0, 0, 0]): []
>>>print("warmup1([]): ", warmup1([]))
warmup1([]): []
"""


""" Warm up 2: given a sequence of numbers, sort in descending order
"""

def warmup2(numbers):
    numbers.sort(reverse=True)
    return numbers

"""
print("warm up 2: sort descending")
>>>print("warmup2([5, 3, 0, 2, 6, 2, 7, 2, 5]): ", warmup2([5, 3, 0, 2, 6, 2, 7, 2, 5]))
[7, 6, 5, 3, 2, 2, 2, 0]
>>>print("warmup2([4, 0, 0, 1, 3]): ", warmup2([4, 0, 0, 1, 3]))
[4, 3, 1, 0, 0]
>>>print("warmup2([0, 0, 0]): ", warmup2([0, 0, 0]))
[0, 0, 0]
>>>print("warmup2([]): ", warmup2([]))
[]
"""


""" Warm up 3: length check, Given a number N and a sequence of numbers, return
    true if N is greater than the number of numbers (i.e. the length of the 
    sequence), and false if N is less than or equal to the number of numbers. 
    For instance, given 7 and [6, 5, 5, 3, 2, 2, 2], you would return false, 
    because 7 is less than or equal to 7.
"""

def warmup3(n, numbers):
    if n > len(numbers):
        return True
    else:
        return False

"""
print("warm up 3: length check")
>>>print("warmup3(7, [6, 5, 5, 3, 2, 2, 2]): ", warmup3(7, [6, 5, 5, 3, 2, 2, 2]))
warmup3(7, [6, 5, 5, 3, 2, 2, 2]): False
>>print("warmup3(5, [5, 5, 5, 5, 5]): ", warmup3(5, [5, 5, 5, 5, 5]))
warmup3(5, [5, 5, 5, 5, 5]): False
>>>print("warmup3(5, [5, 5, 5, 5]): ", warmup3(5, [5, 5, 5, 5]))
warmup3(5, [5, 5, 5, 5]): True
>>>print("warmup3(3, [1, 1]): ", warmup3(3, [1, 1]))
warmup3(3, [1, 1]): True
>>>print("warmup3(1, []): ", warmup3(1, []))
warmup3(1, []): True
>>>print("warmup3(0, []): ", warmup3(0, []))
warmup3(0, []): False
"""

""" Warm up 4: front elimination, given a number N, and a sequence in descding
    order, subtract 1 front each of the 1st N elements in the sequence. Eg, 
    given N=4 and [5, 4, 3, 2, 1], subtract 1 from 5, 4, 3, and 2
"""

def warmup4(n, numbers):
    subtracted_numbers = numbers[:n]
    subtracted_numbers = [x-1 for x in subtracted_numbers]
    subtracted_numbers += numbers[n:]
    return subtracted_numbers

    """ reddit comments, variable names changed for consistency
    def warmup4(n, numbers):
    new_list = []
    for item in sorted_list[:n]:
        new_list.append(item - 1)
    new_list += sorted_list[n:]
    return new_list
    """
"""
>>>print("warmup4(4, [5, 4, 3, 2, 1]): ", warmup4(4, [5, 4, 3, 2, 1]))
warmup4(4, [5, 4, 3, 2, 1]): [4, 3, 2, 1, 1]
>>>print("warmup4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]): ", warmup4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]))
warmup4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]): [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2]
>>>print("warmup4(1, [10, 10, 10]): ", warmup4(1, [10, 10, 10]))
warmup4(1, [10, 10, 10]): [9, 10, 10]
>>>print("warmup4(3, [10, 10, 10]): ", warmup4(3, [10, 10, 10]))
warmup4(3, [10, 10, 10]): [9, 9, 9]
>>>print("warmup4(1, [1]): ", warmup4(1, [1]))
warmup4(1, [1]): [0]
"""

""" Challenge: the Havel-Hakimi algorithm
Perform the Havel-Hakimi algorithm on a given sequence of answers. This 
algorithm will return true if the answers are consistent (i.e. it's 
possible that everyone is telling the truth) and false if the answers are 
inconsistent (i.e. someone must be lying):

1. Remove all 0's from the sequence (i.e. warmup1).

2. If the sequence is now empty (no elements left), stop and return true.

3. Sort the sequence in descending order (i.e. warmup2).

4. Remove the first answer (which is also the largest answer, or tied for the
   largest) from the sequence and call it N. The sequence is now 1 shorter than
   it was after the previous step.

5. If N is greater than the length of this new sequence (i.e. warmup3), stop and 
   return false.

6. Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).

7. Continue from step 1 using the sequence from the previous step.

Eventually you'll either return true in step 2, or false in step 5.
"""

# Run test cases for warmup functions from docstring
import doctest
doctest.testmod()

def challenge(numbers):
        # Remove 0's
        non_zero_numbers = warmup1(numbers)
        # Check for empty list
        if len(non_zero_numbers) == 0:  #if len(numbers) == 0: # or if numbers == []
            return True
        # Sort list descending
        sorted_numbers = warmup2(non_zero_numbers)
        # Remove 1st element of numbers and call it N
        N = sorted_numbers.pop(0)
        # If N is greater than sequence length, return False
        if warmup3(N, sorted_numbers) == True:
            return False
        #subtract 1 from 1st N elements
        subtracted_numbers = warmup4(N, sorted_numbers)
        return challenge(subtracted_numbers)


print(challenge([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
print(challenge([4, 2, 0, 1, 5, 0]))
print(challenge([3, 1, 2, 3, 1, 0]))
print(challenge([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
print(challenge([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))
print(challenge([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))
print(challenge([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))
print(challenge([2, 2, 0]))
print(challenge([3, 2, 1]))
print(challenge([1, 1]))
print(challenge([1]))
print(challenge([]))


""" From reddit comments:
def hh(seq):
    seq = [n for n in seq if n != 0]
    if not seq:
        return True

    seq.sort(reverse=True)
    n = seq.pop(0)

    if n > len(seq):
        return False

    seq = [x - 1 for x in seq[:n]] + seq[n:]
    return hh(seq)
"""

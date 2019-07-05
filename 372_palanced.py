"""Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false

"""


"""Optional bonus
Given a string containing only lowercase letters, find whether every letter that appears in the string appears the same number of times. Don't forget to handle the empty string ("") correctly!

balanced_bonus("xxxyyyzzz") => true
balanced_bonus("abccbaabccba") => true
balanced_bonus("xxxyyyzzzz") => false
balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
balanced_bonus("pqq") => false
balanced_bonus("fdedfdeffeddefeeeefddf") => false
balanced_bonus("www") => true
balanced_bonus("x") => true
balanced_bonus("") => true
Note that balanced_bonus behaves differently than balanced for a few inputs, e.g. "x".
"""

def balanced(string):
    x_count, y_count = 0, 0
    for char in string:
        if char == 'x':
            x_count = x_count + 1
        elif char =='y':
            y_count = y_count + 1
        else:
            print("Strings may only contain 'x' or 'y'. Exiting")
            exit()
    if x_count == y_count:
        return True
    else:
        return False

# From reddit comments
def balanced_bonus(string):
	if len(string) == 0:
		return True

	letters = {}
	for letter in string:
		try:
			letters[letter] += 1
		except:
			letters[letter] = 1

	return len(set(letters.values())) == 1


print("balanced(\"xxxyyy\"): ", balanced("xxxyyy"))
print("balanced(\"yyyxxx\"): ", balanced("yyyxxx"))
print("balanced(\"xxxyyyy\"): ", balanced("xxxyyyy"))
print("balanced(\"yyxyxxyxxyyyyxxxyxyx\"): ", balanced("yyxyxxyxxyyyyxxxyxyx"))
print("balanced(\"xyxxxxyyyxyxxyxxyy\"): ", balanced("xyxxxxyyyxyxxyxxyy"))
print("balanced(\"\"): ", balanced(""))
print("balanced(\"x\"): ", balanced("x"))
#print("balanced(\"xxxyyya\"): ", balanced("xxxyyya"))

print("balanced_bonus(\"xxxyyyzzz\"): ", balanced_bonus("xxxyyyzzz"))
print("balanced_bonus(\"abccbaabccba\"): ", balanced_bonus("abccbaabccba"))
print("balanced_bonus(\"xxxyyyzzzz\"): ", balanced_bonus("xxxyyyzzzz"))
print("balanced_bonus(\"abcdefghijklmnopqrstuvwxyz\"): ", balanced_bonus("abcdefghijklmnopqrstuvwxyz"))
print("balanced_bonus(\"pqq\"): ", balanced_bonus("pqq"))
print("balanced_bonus(\"fdedfdeffeddefeeeefddf\"): ", balanced_bonus("fdedfdeffeddefeeeefddf"))
print("balanced_bonus(\"www\"): ", balanced_bonus("www"))
print("balanced_bonus(\"\"): ", balanced_bonus(""))
print("balanced_bonus(\"x\"): ", balanced_bonus("x"))


# one line solution from reddit:
#def balanced(string):
#    return string.lower().count("x") == string.lower().count("y")
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


""" from reddit commentss
class NonIntegralException(Exception):
	pass

def add(a, b):
	return a + b

def sub(a, b):
	dif = 0
	if b < a:
		incr = 1
	else:
		incr = -1 # cheating
		a, b = b, a
	while b < a:
		dif += incr
		b += 1
	return dif

def mult(a, b):
	if a < 0 and b < 0:
		a = sub(0, a)
		b = sub(0, b)
	elif a < 0:
		a, b = b, a
	i = r = 0
	while i < a:
		r += b
		i += 1
	return r

def div(a, b):
	if b == 0:
		raise ZeroDivisionError("Cannot divide by zero")
	if a < 0 and b < 0:
		a = sub(0, a)
		b = sub(0, b)
	if a >= 0 and b >= 0:
		incr = 1
	elif a < 0:
		a = sub(0, a)
		incr = -1
	elif b < 0:
		b = sub(0, b)
		incr = -1
	r = 0
	old_t = 0
	t = b
	while a >= t:
		old_t = t
		t += b
		r += incr
	if old_t != a:
		raise NonIntegralException("Result is not a whole number")
	return r

def exp(a, b):
	if b < 0:
		if a == 0:
			raise ZeroDivisionError("Cannot divide by zero")
		raise NonIntegralException("Result is not a whole number")
	if b == 0:
		return 1
	r = a
	i = 1
	while i < b:
		r = mult(r, a)
		i += 1
	return r

operations = {
	"+": add,
	"-": sub,
	"*": mult,
	"/": div,
	"^": exp,
}

def adding_calculate(txt):
	a, op, b = txt.split()
	a, b = int(a), int(b)
	return operations[op](a, b)

if __name__ == "__main__":
	while True:
		try:
			print(adding_calculate(input()))
		except KeyError as e:
			print("Unknown operator:", e)
		except Exception as e:
			print(e)
		except KeyboardInterrupt as e:
			exit()

"""

# Check to see if a number is in the form (2^n) - 1

def is_of_form(x):

	x = x - 1

	if x % 2 != 0:
		return False

	else:
		while x != 1:
			x = x / 2
			if x == 1:
				return True
			if x % 2 != 0:
				return False

x = 16
print(is_of_form(x))
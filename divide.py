
# Implement a divide function without using /, %, *, etc.

# The fraction part of answers that aren't whole numbers are not simplified,
# but that's just gonna have to do for now lol

def divide(x, y):

	solution = ""
	
	# If only one of the divisor or dividend is negative, make the
	# solution negative

	if (x < 0 and y > 0) or (x > 0 and y < 0):
		solution += "-"

	x = abs(x)
	y = abs(y)

	if y == 0:
		return "Undefined"

	if x == 0:
		return 0

	if y == x:
		solution += str(1)
		return solution

	if x < y:
		fraction = str(x)
		fraction += "/"
		fraction += str(y)
		solution += fraction
		return solution

	original_y = y

	for i in range(2, x):

		y += original_y
		
		if y == x:
			solution += str(i)
			return solution
		
		if y > x:
			modulo = abs(x - (y - original_y))
			solution += str(i - 1) + " " + divide(modulo, original_y)
			return solution

x = 90
y = 88
print(divide(x, y))

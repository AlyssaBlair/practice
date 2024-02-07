
# Implement a divide function without using /, %, etc.

# I can't figure out how to account for negative numbers in an efficient 
# way without doing a bunch of if statements. I'm sure it has to do with 
# the abs() function but I can't figure out which values need to be the 
# absolute value, I'll come back to this with fresh eyes later. Also the
# fraction part of answers that aren't whole numbers are not simplified,
# but that's just gonna have to do for now lol

def divide(x, y):

	if y == 0:
		return "Undefined"

	if y == x:
		return 1

	if x < y:
		fraction = str(x)
		fraction += "/"
		fraction += str(y)
		return fraction

	original_y = y

	for i in range(2, x):

		y += original_y
		
		if y == x:
			return i
		
		if y > x:
			modulo = abs(x - (y - original_y))
			solution = str(i - 1) + " " + divide(modulo, original_y)
			return solution 

x = 20
y = 6
print(divide(x, y))
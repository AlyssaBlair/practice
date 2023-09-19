
#I can't figure out how to account for negative numbers in an efficient way without doing a bunch of if statements. I'm sure it has to do with the abs() function but I can't figure out which values need to be the absolute value, I'll come back to this with fresh eyes later.

def divide(x, y):

	if y == 0:
		return "Undefined"

	original_y = y

	for i in range(2, x):
	
		y += original_y
		#print(y)
		
		if y > x - original_y:
			return i + ((x % original_y) / original_y)

x = 36
y = 2
print(divide(x, y))
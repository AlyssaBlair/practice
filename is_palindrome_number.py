
# Check to see if a number is a palindrome. For
# example, 4678764 is a palindrome number.
# 467876 is not.

def is_palindrome_number(x):

	x_string = str(x)
	left = 0
	right = len(x_string) - 1
	
	while left <= right:
		if x_string[left] != x_string[right]:
			return False
		else:
			left += 1
			right -= 1
	return True	

x = 4789874
print(is_palindrome_number(x))
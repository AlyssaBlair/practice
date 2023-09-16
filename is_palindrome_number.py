
def is_palindrome_number(x):

	x_string = str(x)
	print(x_string)
	left = 0
	right = len(x_string) - 1
	
	while left <= right:
		if x_string[left] != x_string[right]:
			return False
		else:
			left += 1
			right -= 1
	return True	

x = 478987
print(is_palindrome_number(x))
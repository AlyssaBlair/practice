
# Write a function to print the first letter of every word in a 
# sequence of words.

def print_first_letters(s):

	split_string = s.split()

	for i in range(0, len(split_string)):
		print(split_string[i][0])

s = "This is a test of this code"
print_first_letters(s)
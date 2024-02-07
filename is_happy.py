
# Checks to see if a number is "happy." A number is called happy if it leads 
# to 1 after a sequence of steps wherein each step number is replaced by the 
# sum of the squares of its digits. That is, if we start with a "happy" number 
# and keep replacing it with the sum of its digits squares, we reach 1. For 
# example, 19 is "happy", because 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 
# and 1^2 + 0^2 + 0^2 = 1. As we reached to 1, 19 is a "happy" number.

def is_happy(n, map_new_numbers):

	n_as_string = str(n)
	new_number = 0
	
	for i in range(0, len(n_as_string)):
		
		new_number += int(n_as_string[i]) * int(n_as_string[i])

		if i == len(n_as_string) - 1:
			
			if new_number in map_new_numbers:
				return False

			if new_number not in map_new_numbers:
				map_new_numbers[new_number] = 1
				
			if new_number == 1:
				return True

			result = is_happy(new_number, map_new_numbers)

			if result:
				return True

	return False
			
n = 19
print(is_happy(n, {}))

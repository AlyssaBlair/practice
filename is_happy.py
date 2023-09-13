
def is_happy(n, map_new_numbers):

	n_as_string = str(n)
	new_number = 0
	
	for i in range(0, len(n_as_string)):
		new_number += int(n_as_string[i]) * int(n_as_string[i])
		if i == len(n_as_string) - 1:
			#print("new number is", new_number)
			if new_number in map_new_numbers:
				#print("new number in map already, False")
				return False
			if new_number not in map_new_numbers:
				map_new_numbers[new_number] = 1
				#print(map_new_numbers)
			if new_number == 1:
				#print("we made it here, new number is 1, True")
				return True
			result = is_happy(new_number, map_new_numbers)
			if result:
				return True
	return False
			
n = 19
print(is_happy(n, {}))
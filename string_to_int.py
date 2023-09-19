
#Convert a string to an int without using any built in conversion functions. Assume input is a valid number with no letters. I have included the case for a negative number by taking the negative sign away, then converting to an int, then at the end multiplying by -1 if the original string had a "-" as the first element. This will also account for other non alpanum characters and return an integer that removes those elements, but this will not account for letters being in the original string

def string_to_int(s):

	new_string = ""

	for i in range(0, len(s)):
		if s[i].isalnum():
			new_string += s[i]

	int_map = {
		"0": 0,
		"1": 1,
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
	}

	new_int = 0

	for i in range(0, len(new_string)):

		new_int += int_map[new_string[(len(new_string) - 1) - i]] * pow(10, i)

	if s[0] == "-":
		new_int *= -1

	return new_int

s = "0"
print(string_to_int(s))

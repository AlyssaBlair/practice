
def is_valid(s):

	valid_characters = {
		"(": ")",
		"[": "]",
		"{": "}"
	}

	stack = []

	for i in range(0, len(s)):
		if s[i] in valid_characters:
			stack.append(s[i])
		elif s[i] in valid_characters.values():
			if stack == []:
				return False
			if valid_characters[stack.pop()] != s[i]:
				return False
	return len(stack) == 0
	
s = "(][]){}"
print(is_valid(s))
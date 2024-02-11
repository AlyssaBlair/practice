
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

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
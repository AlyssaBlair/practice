
# Write a program that returns the length of the last word
# of a sequence of words.

def length_of_last_word (s):

	splitString = s.split()
	letterCount = 0
	lengthOfSplitString = len(splitString)
	lastWord = splitString[lengthOfSplitString - 1]
	return len(lastWord)

s = "luffy is still joyboy"
print(length_of_last_word(s))
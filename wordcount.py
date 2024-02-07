
# This code checks to see how many times a given word appears in a block 
# of text. This code disregards upper vs. lower case.

def wordcount(s, t):

	split_string = s.lower()
	split_string = split_string.split()
	lower_t = t.lower()
	wordcount = 0

	for i in range(0, len(split_string)):
		if split_string[i] == lower_t:
			wordcount += 1

	return wordcount

s = "Count these words how many times I say the word count count Count"
t = "Count"
print(wordcount(s, t))
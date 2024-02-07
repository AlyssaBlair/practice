
# Given two strings s and t, determine if they are isomorphic. 

# Two strings s and t are isomorphic if the characters in s can 
# be replaced to get t. All occurrences of a character must be 
# replaced with another character while preserving the order of 
# characters. No two characters may map to the same character, 
# but a character may map to itself. 

# Here’s an example of two isomorphic strings: s = “paper” t = “title”
# In this example, the characters in s can be replaced to get t 
# while preserving the order of characters, and no two characters 
# map to the same character. Specifically, the mapping would be:
# p -> t, a -> I, e -> l, r -> e Therefore, s and t are isomorphic.

def is_isomorphic(s, t):

	mapST = {}
	mapTS = {}

	for i in range(0, len(s)):
		if (s[i] in mapST and mapST[s[i]] != t[i]) or (t[i] in mapTS and mapTS[t[i]] != s[i]):
			return False
		mapST[s[i]] = t[i]
		mapTS[t[i]] = s[i]
	return True

s = "paper"
t = "title"
print(is_isomorphic(s, t))
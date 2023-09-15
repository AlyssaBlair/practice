
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
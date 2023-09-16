
#Given two strings with the same characters except for one additional character in one string, return that additional character.

def extra_character(s, t):

	map_shorter = {}
	map_longer = {}
	longer = ""
	shorter = ""
	
	if len(s) > len(t):
		longer = s
		shorter = t
	else:
		longer = t
		shorter = s

	for i in range(0, len(shorter)):
			if shorter[i] in map_shorter:
				map_shorter[shorter[i]] += 1
			else:
				map_shorter[shorter[i]] = 1

	for i in range(0, len(longer)):
			if longer[i] in map_longer:
				map_longer[longer[i]] += 1
			else:
				map_longer[longer[i]] = 1

	for i in range(0, len(longer)):
		if longer[i] not in map_shorter:
			return longer[i]
		else:
			if map_longer[longer[i]] > map_shorter[longer[i]]:
				return longer[i]
			
s = "happpy"
t = "happy"
print(extra_character(s, t))


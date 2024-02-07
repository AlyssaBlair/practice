
# Write a function that returns true if a given array contains duplicates 
# within k distance. Given the array [1, 1, 3, 1, 2, 3, 1] and k = 1, the
# function should return True because of the consecutive 1s (they are 
# within 1 element of each other). Given [3, 7, 5, 6, 9, 2, 7] and k = 4,
# the function should return False, because while there are duplicate 7s, 
# they are 5 elements away from each other.

def contains_nearby_duplicate(nums, k):

	duplicates = {}

	for i in range(0, len(nums)):
		
		if nums[i] not in duplicates:
			duplicates[nums[i]] = 1
		else:
			duplicates[nums[i]] += 1
			
			for x in range(1, k + 1):
				if nums[i] == nums[i - x]:
					return True
	return False

nums = [3, 7, 5, 6, 9, 2, 7]
k = 4
print(contains_nearby_duplicate(nums, k))
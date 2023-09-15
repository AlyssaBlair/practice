
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

nums = [1, 1, 3, 1, 2, 3, 1]
k = 2
print(contains_nearby_duplicate(nums, k))
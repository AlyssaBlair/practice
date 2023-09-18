
#assuming each input has exactly one solution, cannot use same element twice, returning the index of the two numbers that create the sum

def two_sum(nums, target):

	sumsMap = {}

	for i in range(0, len(nums)):
		if nums[i] <= target:
			sumsMap[nums[i]] = target - nums[i]
	
	#search nums for the target minus the number

	for i in range(0, target):
		if target - nums[i] in sumsMap.keys() and nums[i] != target / 2:
			for j in range(0, len(nums)):
				if nums[j] == target - nums[i]:
					return i, j			

nums = [2, 11, 15, 7]
target = 9
print(two_sum(nums, target))

# Assuming each input has exactly one solution, and cannot use 
# the same element twice, return the index of the two numbers 
# in the array that create the target sum. This code does not 
# account for a situation in which the target cannot be reached 
# by adding exactly two of the elements of the array together. 
# This assumes there is exactly one solution.

def two_sum(nums, target):

	sumsMap = {}

	for i in range(0, len(nums)):
		if nums[i] <= target:
			sumsMap[nums[i]] = target - nums[i]
	
	# search nums for the target minus the number

	for i in range(0, target):
		if target - nums[i] in sumsMap.keys() and nums[i] != target / 2:
			for j in range(0, len(nums)):
				if nums[j] == target - nums[i]:
					return i, j			

nums = [2, 11, 15, 7]
target = 22
print(two_sum(nums, target))
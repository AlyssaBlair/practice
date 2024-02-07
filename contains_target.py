
# Use binary search to check if a given array of integers 
# contains a target integer.

def contains_target(nums, target):

	# First we'll sort the array in ascending order

	for i in range(0, len(nums)):
	
		for j in range(i + 1, len(nums)):
	
			if nums[j] < nums[i]:
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp

	# Now we'll use binary search to find the target

	left = 0
	right = len(nums) - 1

	while left <= right:
		
		mid = (right + left) // 2

		if nums[mid] == target:
			return True

		if nums[mid] < target:
			left = mid + 1

		if nums[mid] > target:
			right = mid - 1

	return False
	
nums = [0, 6, 7, 3, 6]
target = 20
print(contains_target(nums, target))

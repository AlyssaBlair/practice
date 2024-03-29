
# Given a sorted array of distinct integers and a target 
# value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted 
# in order.

def search_insert(nums, target):

	left = 0
	right = len(nums) - 1

	while left <= right:
		mid = (right + left) // 2
		if nums[mid] == target:
			return mid
		if target > nums[mid]:
			left = mid + 1
		if target < nums[mid]:
			right = mid - 1
	return left

nums = [1, 3, 4, 6]
target = 11
print(search_insert(nums, target))
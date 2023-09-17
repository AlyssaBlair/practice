
#Given an array of positive integers and a target integer, find if there is a consecutive subarray that sums to the target. E.g, given {5,6,4,12}, findsum(10)=true, findsum(18)=false.

def consecutive_sum(nums):

	for i in range(0, len(nums)):
		
		if nums[i] <= target:

			if i > 0:
				if nums[i - 1] == target - nums[i]:
					return True
			if i < len(nums) - 1:
				if nums[i + 1] == target - nums[i]:
					return True
	return False
	
	print(possible_combos)
	
nums = [5, 6, 4, 12]
target = 10
print(consecutive_sum(nums))
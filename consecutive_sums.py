
#Given an array of positive integers and a target integer, find if there is a consecutive subarray that sums to the target. E.g, given {5,6,4,12}, findsum(10)=true, findsum(18)=false.

def consecutive_sum(nums):

	possible_combos = {}

	for i in range(0, len(nums)):
		
		if nums[i] <= target:
			possible_combos[nums[i]] = target - nums[i]

			if i > 0:
				if nums[i - 1] == possible_combos[nums[i]]:
					return True
			if i < len(nums) - 1:
				if nums[i + 1] == possible_combos[nums[i]]:
					return True
	return False
	
	print(possible_combos)
	
nums = [6, 1, 6, 7]
target = 12
print(consecutive_sum(nums))
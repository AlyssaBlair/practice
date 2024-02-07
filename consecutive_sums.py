
#Given an array of positive integers and a target integer, find if there 
#is a consecutive subarray that sums to the target. 
#E.g, given {5,6,4,12}, findsum(10)=true, findsum(18)=false.

#I'm realizing now that this code only checks if there is a consecutive 
#subarray of size two that sums to the target. So setting the target to 
#14 with the array [5, 6, 4, 12] returns False, when it should return 
#True becuase 5 + 6 + 4 = 14. I'll have to keep working on this one.

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
	
nums = [5, 6, 4, 12]
target = 14
print(consecutive_sum(nums))

# Return the ranges of numbers covered consecutively by the input array. 
# Example: Input: nums = [0,1,2,4,5,7], Output: ["0->2","4->5","7"]

def summary_ranges(nums):

	current_range = [nums[0]]
	final_array = []

	for i in range(1, len(nums)):
		if nums[i] - nums[i - 1] == 1:
			current_range.append(nums[i])
		else:
			final_array.append(current_range)
			current_range = [nums[i]]

	final_array.append(current_range)

	for i in range(0, len(final_array)):

		if len(final_array[i]) == 1:
			print(final_array[i][0])
		else:
			print(final_array[i][0], "->", final_array[i][len(final_array[i]) - 1])

nums = [0, 3, 4, 5, 6, 8, 9, 11]
summary_ranges(nums)
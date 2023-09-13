
def summary_ranges(nums):

	range_array = []
	final_array = []
	
	for i in range(0, len(nums) - 1):	
		if nums[i] != nums[i + 1] - 1:
			range_array = []
			range_array.append(nums[i + 1])
			final_array.append(range_array)
			print(range_array)

		elif nums[i] == nums[i + 1] - 1:
			if nums[i] not in range_array:
				final_array.append(range_array)
				range_array.append(nums[i])
			range_array.append(nums[i + 1])
			print(range_array)
	for i in range(0, len(final_array)):
		if len(final_array[i]) == 1:
			print(final_array[i], "has one number")
		else:
			final_array[i] = [final_array[i][0], "->", final_array[i][len(final_array[i]) - 1]]
	print(final_array)

nums = [0, 3, 4, 5, 6, 8, 9]
summary_ranges(nums)

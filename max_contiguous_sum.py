
#Write a function to find the maximum sum of any contiguous sub array of an array of integers

def max_contiguous_sum(nums):

	contiguous_numbers = [nums[0]]
	sets_array = []
	sums_array = []

	for i in range(1, len(nums)):
		
		if nums[i] - nums[i - 1] == 1:
			contiguous_numbers.append(nums[i])
		else:
			sets_array.append(contiguous_numbers)
			contiguous_numbers = [nums[i]]

	sets_array.append(contiguous_numbers)

	print(sets_array)

	for i in range(0, len(sets_array)):
		
		sum = 0

		for j in range(0, len(sets_array[i])):
			sum += sets_array[i][j]
			
		sums_array.append(sum)

	highest_sum = sums_array[0]

	print(sums_array)
	
	for i in range(1, len(sums_array)):
		if sums_array[i] > sums_array[i - 1]:
			highest_sum = sums_array[i]

	print(highest_sum)

nums = [0, 1, 3, 4, 5, 6, 8, 9]
max_contiguous_sum(nums)

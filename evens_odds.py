
#Take an unordered array of ints and put all the evens first and in ascending order, then all the odds in ascending order in one array

def evens_odds(nums):

	#Put the even elements first and the odd elements after, without sorting

	for i in range(0, len(nums)):
		
		for j in range(i + 1, len(nums)):

			if nums[i] % 2 != 0 and nums[j] % 2 == 0:
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp

	#Now sort the elements in ascending order, keeping the even numbers first

	for i in range(0, len(nums)):
		
		for j in range(i + 1, len(nums)):

			#If the number to the right of the number we are looking at is odd and the number we are looking at is even, we switch i to j so we keep the odds after the evens

			if nums[j] % 2 != 0 and nums[i] % 2 == 0:
				i = j

			if nums[j] <= nums[i]:
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp
	
	print(nums)

nums = [9, 3, 4, 7, 6]
evens_odds(nums)

class Solution:
	# binary search uses 3 indicies
	def searchInsert(self, nums: List[int], target: int) -> int:
		start_index = 0
		end_index = len(nums) - 1

		while start_index <= end_index:
			print('start_index', start_index)
			print('e', end_index)
			mid_index = start_index + (end_index - start_index) // 2
			print('mid_index', mid_index)
			if target > nums[mid_index]:
				start_index = mid_index + 1
			elif target < nums[mid_index]:
				end_index = mid_index - 1
			else:
				return mid_index

		return start_index
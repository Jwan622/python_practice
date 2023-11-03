class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		final = []
		# return [ele if index != len(digits) - 1 else ele + 1 for index, ele in enumerate(digits)]
		# for i in range(len(digits) - 1, -1, -1): # the last argument in the range function is the step
		#     print('i', i)
		#     if digits[i] == 9:
		#         digits[i] = 0
		#     else:
		#         digits[i] = digits[i] + 1
		#         return digits
		# return [1] + digits

		# List -> Number
		n = 0
		for ele in digits:
			# This will have the effect of shifting digits of the number variable to the left by one place and adding the upcoming digit to the right.
			n = (n * 10) + ele

		n = n + 1  # because we need to increment the number

		# Number -> List
		digits = []
		while n > 0:
			digits.insert(0, n % 10)
			n //= 10
		return digits
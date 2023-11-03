class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		white_space = ' '
		length_string = 0

		for index, letter in enumerate(s):
			if letter != white_space and s[index - 1] == white_space:
				length_string = 1
			elif letter != white_space and s[index - 1] != white_space:
				length_string += 1

		return length_string

s1 = Solution().lengthOfLastWord('hello there')
print('s1', s1) # 5
s2 = Solution().lengthOfLastWord('hello there    ')
print('s2', s2) # 5
s3 = Solution().lengthOfLastWord('    my name is Jeff ')
print('s3', s3) # 4
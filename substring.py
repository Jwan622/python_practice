class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		start_index = -1
		bad_start_index = -1
		haystack_index = 0
		needle_index = 0

		if len(needle) > len(haystack):
			return -1

		while haystack_index < len(haystack):
			if needle_index == len(needle):
				return start_index

			if haystack[haystack_index] == needle[needle_index]:
				# print('equal haystackindex', haystack_index)
				# print('equal needle_index', needle_index)
				if start_index == -1 and haystack_index < len(haystack) - len(
						needle) + 1 and haystack_index == bad_start_index:
					haystack_index += 1
				elif start_index == -1 and haystack_index < len(haystack) - len(
						needle) + 1 and haystack_index != bad_start_index:
					start_index = haystack_index
					bad_start_index = haystack_index
				haystack_index += 1
				needle_index += 1
				continue
			elif haystack[haystack_index] != needle[needle_index] and start_index != -1:
				# print('reset haystackindex', haystack_index)
				# print('reset needleindex', needle_index)
				start_index = -1
				needle_index = 0
				haystack_index -= 1
				continue
			else:
				# print('else haystackindex', haystack_index)
				# print('else needleindex', needle_index)
				if haystack_index < len(haystack): haystack_index += 1
				continue

		return start_index
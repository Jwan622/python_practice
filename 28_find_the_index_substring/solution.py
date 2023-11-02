class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		start_index = -1
		bad_start_index = -1
		haystack_index = 0
		needle_index = 0

		while haystack_index < len(haystack) or needle_index < len(needle):
			if haystack_index == len(haystack):  # once we're past the haystack, the substring cannot be found.
				return -1
			if needle_index == len(needle):
				return start_index
			if needle_index == len(haystack):  # the needle cannot be greater than the haystack
				return -1

			if haystack[haystack_index] == needle[needle_index]:
				if haystack_index == bad_start_index:
					haystack_index += 1
					continue

				if start_index == -1 and haystack_index <= len(haystack) - len(
						needle) + 1 and haystack_index != bad_start_index:
					start_index = haystack_index
					bad_start_index = haystack_index  # the possible substring cannot be at this index in haystack
				haystack_index += 1
				needle_index += 1
				continue
			elif haystack[haystack_index] != needle[needle_index] and start_index != -1:
				start_index = -1
				needle_index = 0
				haystack_index = bad_start_index + 1  # slide the window forward in the haystack to where we last attempting to find the substring + index
				continue
			else:
				if haystack_index < len(haystack): haystack_index += 1
				continue

		return start_index
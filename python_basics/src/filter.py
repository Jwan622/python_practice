import math


def is_positive(num):
	return num >= 0


def sanitized_sqrt(numbers):
	cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
	return list(cleaned_iter)


print(sanitized_sqrt([1,3,5,-7,9,10]))
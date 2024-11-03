"""
File: largest_digit.py
Name: Annby
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	n = abs(n)

	if n < 10:
		return n

	last_digit = n % 10
	others_digits = n // 10

	max_digit_in_rest = find_largest_digit(others_digits)
	if last_digit > max_digit_in_rest:
		return last_digit
	else:
		return max_digit_in_rest




if __name__ == '__main__':
	main()

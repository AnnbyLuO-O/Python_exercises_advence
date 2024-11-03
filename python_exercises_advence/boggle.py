"""
File: boggle.py
Name: Annby
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	grid = []
	for i in range(4):
		row = input(f'{i + 1} row of letters: ').lower().split()
		if len(row) != 4:
			print("Invalid input. Please enter exactly 4 letters separated by spaces.")
			return
		grid.append(row)
	start = time.time()
	dictionary = read_dictionary()

	found_words = []

	for i in range(4):
		for j in range(4):
			search_words(grid, i, j, "", found_words, dictionary, [])

	for word in found_words:
		print(f'Found "{word}"')

	print(f'There are {len(found_words)} words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	word_list = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				word_list.append(word)
	return word_list


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


def search_words(grid, x, y, current_word, found_words, dictionary, visited):
	if [x, y] in visited:
		return

	current_word += grid[x][y]
	visited.append([x, y])

	if len(current_word) >= 4 and current_word in dictionary and current_word not in found_words:
		found_words.append(current_word)

	if has_prefix(current_word, dictionary):
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
		for dx, dy in directions:
			new_x = x + dx
			new_y = y + dy
			if 0 <= new_x < 4 and 0 <= new_y < 4:
				search_words(grid, new_x, new_y, current_word, found_words, dictionary, visited[:])

	visited.pop()


if __name__ == '__main__':
	main()

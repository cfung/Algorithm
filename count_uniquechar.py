# count the number of unqiue char

# ideas:  use dict to store char as key

# mistake 1: typo on collection(s)
# mistake 2: forgot to strip whitespace
# mistake 3: after splitting on whitespace, forgot to join back as str
# mistake 4: forgot to account for non-char
# mistake 5: forgot else case
# mistake 6: if not in should set value to 1, not +=

from collections import defaultdict
import string
'''
def count_unique(str):

	dict_res = defaultdict(int)

	# loop thru the str
	for char in "".join(str.split(' ')):
		if char not in dict_res and char in string.letters:
			dict_res[char] += 1

	#print "dict..", dict_res
	return len(dict_res.keys())

print count_unique("i am a unqiue person")
print count_unique(" i am a unqiue person ")
print count_unique(" i am a unqiue person? ")
'''

# another variouation: determine if string has all unique characters

# mistake 1: forgot to check if len(str) > 128
# time complexity O(n)

def is_unique(str):

	dict_res = defaultdict(int)

	if len(str) > 128:
		return False

	for char in "".join(str.split(' ')):
		if char not in dict_res and char in string.letters:
			dict_res[char] = 1
		elif char in dict_res and char in string.letters:
			dict_res[char] += 1

	for key in dict_res.keys():
		if dict_res[key] > 1:
			return False

	return True


print is_unique('abc')
print is_unique('abca')

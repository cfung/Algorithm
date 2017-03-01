# count the number of unqiue char

# ideas:  use dict to store char as key

# mistake 1: typo on collection(s)
# mistake 2: forgot to strip whitespace
# mistake 3: after splitting on whitespace, forgot to join back as str
# mistake 4: forgot to account for non-char

from collections import defaultdict
import string
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




'''
Find the first non-repeated (unique) character in a given string. for Example if given String is "Morning" then it should print "M".

Read more: http://javarevisited.blogspot.com/2015/01/top-20-string-coding-interview-question-programming-interview.html#ixzz4aWIWThtT
'''

# mistake 1: on 2nd loop, should loop str instead of d.keys()
# mistkae 2: on 2nd loop, should use enumerate
# mistkae 3: if condition is using str instead of dict
# mistake 4: return result on first found

from collections import defaultdict

def first_non_repeat(str):

	#result = None

	d = defaultdict(int)

	# built dictionary with counts
	for c in str.strip():
		d[c] += 1

	#print ("dict..", d)

	for i, c in enumerate(str.strip()):
		if d[c] == 1:
			return c

	#return result

print (first_non_repeat("Morning"))
print (first_non_repeat("MMMMorning"))
print (first_non_repeat(' geeksforgeeks'))
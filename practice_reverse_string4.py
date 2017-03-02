'''
Given a string, that contains special character together with alphabets ('a' to 'z' and 'A' to 'Z'), 
reverse the string in a way that special characters are not affected.

Input:   str = 'a,b$c'
Output:  str = 'c,b$a'
Note that $ and , are not moved anywhere.  
Only subsequence 'abc' is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
'''

# ideas: 1. loop (backward) thru the str, check if it's letters (string.letters)
#        2. if it is, add it to result str
#        3. return result str 

# mistake 1:  did not add special char
# correction:  create an array -> if it's letter, add to the end

import string
'''
def reverse_nospecial(str):

	s = []
	for x in range(len(str)):
		s.append('0')

	for i in range(len(str)):

		if str[i] in string.letters:
			s[len(str)-1-i] = str[i]
		else:
			s[i] = str[i]

	return "".join(s)

print reverse_nospecial('Ab,c,de!$')
# expected:  ed,c,bA!$
# 00ed,c0!$

'''
# mistake 1: no need to make a copy of str (result) and use that to swap

def reverse_nospecial(str):
	l = 0
	r = len(str) - 1

	#result = str

	str = list(str)
	#result = list(result)

	for i in range(len(str)):

		if str[l] not in string.letters:
			l += 1

		elif str[r] not in string.letters:
			r -= 1

		else:

			str[l], str[r] = str[r], str[l]
			l += 1
			r -= 1

	return "".join(str)


print reverse_nospecial('Ab,c,de!$')

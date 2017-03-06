# reverse a string without using any builtin method

# mistake 1: how to start range() and go reverse?
# mistake 2: forgot to add return

'''
def practice_reverse_string3(str):
	
	result = []

	for i, val in enumerate(str[::-1]):
		result.append(val)

	return "".join(result)

print practice_reverse_string3("cat")
print practice_reverse_string3("iamaverycutecat")
print practice_reverse_string3("I know how it feels.")
'''

'''
Cannot use [::-1] or reverse

http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1

'''
# mistake 1: start and end index
# mistake 2: range returns int rather than value (char), use str[i]

def practice_reverse_string3(str):

	result = []

	# 2nd argument is stop (excludes - so use -1 if it'll stop at 0)
	for i in range(len(str)-1, -1, -1):
		result.append(str[i])

	#print "result..", result
	return "".join(result)

print practice_reverse_string3("cat")
print practice_reverse_string3("iamaverycutecat")
print practice_reverse_string3("I know how it feels.")
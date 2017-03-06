# task: You need to write a program in C, C++, Java or Python to print duplicate characters from a given String,
# for example if String is "Java" then program should print "a". 

# Bonus points if your program is robust and handle different kinds of input e.g. String without duplicate, null or empty String etc
# Read more: http://javarevisited.blogspot.com/2015/01/top-20-string-coding-interview-question-programming-interview.html#ixzz4aP0ZoJ4w

from collections import defaultdict

def print_dup(str):

	res_dict = defaultdict(int)

	for s in str.strip():

		res_dict[s] += 1

	for k in res_dict.keys():

		if res_dict[k] > 1:

			return k

	return "no duplicate"

print (print_dup("java"))
print (print_dup("theone"))
print (print_dup("abcd"))
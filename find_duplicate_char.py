'''
You need to write a program to print all duplicate character and their count

Read more: http://javarevisited.blogspot.com/2015/01/top-20-string-coding-interview-question-programming-interview.html#ixzz4aWRLMYro

ex. Programming

g : 2
r : 2
m : 2
'''
from collections import defaultdict

def find_duplicate(str):

	d = defaultdict(int)

	for s in str.strip():
		d[s] += 1

	for k in d.keys():
		if d[k] > 1:
			print ("%s : %d"%(k, d[k]))

find_duplicate("Programming")

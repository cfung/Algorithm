# task: print all permutations of string

# ideas:  1. turn str into list (?)
#         2. use 2 for loops

# mistake 1: TypeError: cannot concatenate 'str' and 'list' objects (s = list_str[i] + list_str[j:])
# mistake 2: also start j at 0, same as i

# answer: use recursion  O(N!)

# sample input:  'abc'
# sample output: a,ab,abc,ac,acb,b,ba,bac,bc,bca,c,ca,cab,cb,cba

'''
def factorial(n):
	print ("n is..", n)
	if n==1:

		return 1

	else:
		return n * factorial(n-1)

print (factorial(4))
'''


'''
def permutations_all(str):

	result = []

	i = 0

	while i < len(str):

		result.append(permutations_all(str[i+1:]))

		i += 1

	return result

print (permutations_all('abc'))
'''

def permutations(word):
    if len(word)==1:
    	print ("what is [word]", [word])
    	return [word]
 
    #get all permutations of length N-1
    perms=permutations(word[1:])
    print ("what is perms..", perms)
    char=word[0]
    print ("what is char..", char)
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

print (permutations("abc"))

'''
We remove the first character and recurse to get all permutations of length N-1, 
then we insert that first character into N-1 length strings and obtain all permutations of length N .
 The complexity is O(N!) because there are N! possible permutations of a string with length N, so it’s optimal. 
 I wouldn’t recommend executing it for strings longer than 10-12 characters though, 
 it’ll take a long time. Not because it’s inefficient, but inherently there are just too many permutations.


'''


'''
This may seem hard at first but it’s in fact pretty easy once we figure out the logic. 
Let’s say we’re given a string of length N, and we somehow generated some permutations of length N-1. 
How do we generate all permutations of length N? Demonstrating with a small example will help. 
Let the string be ‘LSE’, and we have length 2 permutations ‘SE’ and ‘ES’. 
How do we incorporate the letter L into these permutations? 
We just insert it into every possible location in both strings: beginning, middle, and the end. 
So for ‘SE’ the result is: ‘LSE’, ‘SLE’, ‘SEL’. And for the string ‘ES’ the results is: ‘LES’, ‘ELS’, ‘ESL’. 
We inserted the character L to every possible location in all the strings. This is it!. 
We will just use a recursive algorithm and we’re done. 

Recurse until the string is of length 1 by repeatedly removing the first character, 
this is the base case and the result is the string itself (the permutation of a string with length 1 is itself). 
Then apply the above algorithm, at each step insert the character you removed to every possible location in the recursion results and return. Here is the code:


'''
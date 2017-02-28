# check whether one string is permutation of another
# return True or False 
# ideas:  convert to list, sort them then convert back to str 
from collections import defaultdict
'''
# method 1: sort, O(nlogn)  No mistake!
def permutations(str_A, str_B):
	#print sorted(str_A)

	return "".join(sorted(str_A)) == "".join(sorted(str_B))

print permutations('ithinkthisisme', 'thinkmethisisi')
print permutations('abcd', 'bdea')
print permutations('sumit', 'tiums')
'''
# method 2: using dict (hash table) - O(n)

# mistake 1: result for 2nd case is not correct 
# (Cause:  return True was used in else, should not have else
#          put return True at the end)

# mistake 2: forgot to check len of 2 strings

def permutations(str_A, str_B):

	dict_result = defaultdict(int)

	if len(str_A) != len(str_B):
		return False

	for i in str_A:
		if i in dict_result:
			dict_result[i] += 1
		else:
			dict_result[i] = 1

	#print "before B", dict_result

	for j in str_B:

		if j in dict_result:
			dict_result[j] -= 1
		else:
			dict_result[j] = 1

	#print "after B", dict_result

	for k in dict_result.keys():

		if dict_result[k] != 0:
			return False
		#else:
	return True

print permutations('ithinkthisisme', 'thinkmethisisi')
print permutations('abcd', 'bdea')
print permutations('sumit', 'tiums')
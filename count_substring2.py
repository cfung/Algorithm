

'''
Given a binary string, count number of substrings that start and end with 1. 
For example, if the input string is '00100101', then there are three substrings '1001', '100101' and '101'.

Input:
1
10101

Output:
3

(geekforgeeks)
'''

# ideas:  1. loop thru string and look for '1'
# 		  2. keep track of start position of '1'
# 		  3. find the next occurence of '1'
# 		  4. return the substring
# 	 	  5. count the outside string also

# mistake 1: did not convert input to str, and int has no len()
# mistake 2: did not return correct result
# mistake 3: use int() to cast first input
# mistake 4: this case did not pass

# Input:
# 100100000111111101010010010011010101110110

# Its Correct output is:
# 231

# input:
# 0010110010

# correct output is 6
'''
def count_substring(str):

	start = None
	first_i = None

	count = 0

	#print ("len of str..", len(str))

	for i in range(len(str)):
		#print ("i = ", i)
		if str[i] == '1' and start:
			#print ("first if")
			start = i
			first_i = i
		elif start != 0 and str[i] == '1':
			#print ("2nd if")
			count += 1
		#print ("count during for loop..", count)
	return count
'''

# time complexity = O(n^2)

def count_substring(str):

	count = 0

	for i in range(len(str)):

		for j in range(len(str)):

			if str[i] == '1' and str[j] == '1' and i < j:
				#print (str[i:j+1])
				count += 1

	return count

n = int(input())

for i in range(n):

	s = str(input())
	print (count_substring(s))









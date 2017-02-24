def number_needed(a, b):
    # we should go through both strings, keep track of the # of letter using a dict
    # then compare the difference

    dict_a = {}
    dict_b = {}

    for char in a:
    	# char already in dict
        print "char is...", char
    	if char in dict_a.keys():
            print "key in a exists.."
            dict_a[char] += 1
    	else:
            print "key in a does NOT exist.."
            dict_a[char] = 1

    for char in b:
    	if char in dict_b.keys():
    		dict_b[char] += 1
    	else:
    		dict_b[char] = 1

    #print "dict_a is..", dict_a

    count = 0

    #print sorted(dict_a.keys())
    #print sorted(dict_b.keys())

    # sort the dicts so the keys are alphabetical order
    for char_a, char_b in zip(sorted(dict_a.keys()), sorted(dict_b.keys())):
    	print "what is char_a", char_a
        print "what is char_b", char_b

        if dict_a[char_a] != dict_b[char_b]:

    		count += abs(dict_a[char_a]-dict_b[char_b])

    return count

a = raw_input().strip()
b = raw_input().strip()

# sample input: 
# cde 
# abc

# sample output: 4

print number_needed(a, b)



#  ********************************************************

'''    Python 3 - http://www.practice.geeksforgeeks.org/problem-page.php?pid=88

Given two strings, check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are anagram of each other.

Input:

The first line of input contains an integer T denoting the number of test cases. Each test case consist of two strings in 'lowercase' only, in a separate line.

Output:

Print "YES" without quotes if the two strings are anagram else print "NO".

Constraints:

1 ≤ T ≤ 30

1 ≤ |s| ≤ 100

Example:

Input:
2
geeksforgeeks
forgeeksgeeks
allergy
allergic

Output:
YES
NO
'''
#code
n = int(input().strip())

for num in range(0, n):
    string_A = input().strip()
    string_B = input().strip()

    dict_A = {}
    dict_B = {}

    #if len(string_A) != len(string_B):
    #    print ("NO")
    for char in string_A:
        if char in dict_A.keys():
            dict_A[char] += 1
        else:
            dict_A[char] = 1

    for char in string_B:
        if char in dict_B.keys():
            dict_B[char] += 1
        else:
            dict_B[char] = 1

    if dict_A == dict_B:
        print ("YES")
    else:
        print ("NO")

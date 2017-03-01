
# this problem requires the count of deletion to make 1 string and anagram of another
# https://www.hackerrank.com/challenges/ctci-making-anagrams (cracking the coding interview)

# mistake 1:  should use defaultdict instead of 
# mistake 2:  defaultdict (int)
# mistake 3:  RuntimeError: dictionary changed size during iteration (use keys() instead)
# mistake 4:  looped only 1 dict, need to loop both dicts
# mistake 5:  defaultdict automatically adds keys, so dict_b contains ALL keys

# sample input:
#bugexikjevtubidpulaelsbcqlupwetzyzdvjphn
#lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk

# sample output: 40

from collections import defaultdict

def number_needed(a, b):
    dict_a = defaultdict(int)
    #dict_b = defaultdict(int)

    for char in a:
        
        dict_a[char] += 1

    for char in b:
        
        dict_a[char] -= 1

    count = 0

    for char in dict_a.keys():

        if dict_a[char] != 0:

            count += abs(dict_a[char])

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

Given two strings, check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, 
only the order of characters can be different. For example, "act" and "tac" are anagram of each other.
Input:

The first line of input contains an integer T denoting the number of test cases. Each test case consist of two strings in 'lowercase' only, in a separate line.

Output:

Print "YES" without quotes if the two strings are anagram else print "NO".

Constraints:

1 <= T <= 30

1 <= |s| <= 100

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
'''
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
'''
# *****************************************************************
'''
# Another method:  sort both strings and check if they're equal

def check_anagram_by_sort(string_1, string_2):
    return sorted(string_1) == sorted(string_2)

print check_anagram_by_sort("abcd", "kkoo")

'''
'''
# ******************  Anagram (compare each string) ***************
# https://www.hackerrank.com/challenges/anagram

mistake 1: loop thru for loop used in...X instead of range()
mistake 2: line[len(line)+1:]  (correct:  line[len(line)/2 ])
mistake 3: should NOT do "plus 1 "to start string_B: line[len(line)/2 + 1])
mistake 4: remove string by [::], case where last element to remove FAIL
mistake 5: should create new string with removed idx this way:  newstr = input_str[:idx] + input_str[idx+1:]
mistake 6: forgot to check if string is odd.  If odd, cannot be anagram

# featured solution

from collections import Counter
for _ in range(input()):
    s = raw_input()
    if len(s)%2 == 1:
        print "-1"
        continue
    temp = Counter(s[0:len(s)/2]) - Counter(s[len(s)/2:])
    print sum(temp.values())

'''




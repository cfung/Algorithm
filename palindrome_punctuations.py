# Leetcode: https://leetcode.com/problems/valid-palindrome/description/
# mistake 1: use .join() to remove whitespace
# mistake 2: only used .strip(), did not consider whitespace in middle
# mistake 3: did not know how to use maketrans() and translate()

import string

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    translation = s.replace(" ", "").maketrans("","", string.punctuation)
    #print("translation: ", translation)
    #print(s.replace(" ", "").translate(translation).lower())
    #print(s.replace(" ", "").translate(translation)[::-1].lower())
    #print("1", s.replace(" ", "").maketrans("","", string.punctuation).lower())
    #print("2", s.replace(" ", "")[::-1].maketrans("", "", string.punctuation).lower())
    return s.replace(" ", "").translate(translation).lower() == s.replace(" ", "").translate(translation)[::-1].lower()


assert isPalindrome("A man, a plan, a canal: Panama") == True    
assert isPalindrome("race a car") == False    
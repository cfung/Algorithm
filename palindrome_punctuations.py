


def isPalindrome(self, s):
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

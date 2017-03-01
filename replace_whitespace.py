# replace whitespace with %20
# ideas:  1. loop thru string, split on whitespace
#         2. add the strings back and append with "%20"

# mistake 1:  forgot to account cases where beginning and end has many whitespaces

def replace_whitespace(str):

	list_result = str.strip().split(' ')

	return "%20".join(list_result)


print replace_whitespace("I am a huge fan.")
print replace_whitespace("       Mr John Smith           ")

'''
def urlifyString(str):
    res = ''
    start = False
    str = str.strip() # Removes white space from the beginning and end of the string
    for char in str:
        if(char == ' '):
            res += '%20'
        else: res += char
    return res
 
print urlifyString("       Mr John Smith           ")
'''
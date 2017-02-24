'''Given a String of length N reverse the words in it. Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases. Each case contains a string containing spaces and characters.
 

Output:
For each test case, output a single line containing the reversed String.

Constraints:
1<=T<=10
1<=Lenght of String<=2000


Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr

'''
# mistake 1:  thought this was same as reversing each substring

# ideas:  
# 1. go backward when looping
# 2. add to the pre-existing empty string + ,
# 3. at the end of the loop, don't add ,

#  Use Python 3

n = int(input())

input_list = []

for i in range(0, n):
	user_input = input().strip()
	input_list.append(user_input)

for line in input_list:

	result_string = ""

	for idx, substring in enumerate(line.split('.')[::-1]):
		if idx == len(line.split('.')) - 1:
			result_string += substring
		else:
			result_string += substring
			result_string += '.'

	print (result_string)

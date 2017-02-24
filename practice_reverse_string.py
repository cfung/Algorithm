'''
Given a String of length N reverse each word in it. Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases. Each case contains a string containing dots and characters.
 

Output:
For each test case, output a String in single line containing the reversed words of the given String.

Constraints:
1<=T<=10
1<=Length of String<=2000


Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
i.ekil.siht.margorp.yrev.hcum
rqp.onm

'''

# make 3 mistakes
# mistake 1:  . at the end (also made this mistake before)
# mistake 2:  used len(mystring) instead of len(mystring.split('.'))
# mistake 3:  forgot to -1 in checking the length
# mistake 2:  python 3: forgot to use for loop to get input()
# mistake 3:  python 3: forgot to create empty list

n = int(input())
#print n
input_list = []
for line in range(0, n):
	line_input = input().strip()
	input_list.append(line_input)


for mystring in input_list:

	reversed_string = ""

	for idx, substring in enumerate(mystring.split('.')):
		#print ("length...", len(mystring.split('.')))
		#print ("idx is...%d...%s"% (idx, substring))
		if idx == len(mystring.split('.'))-1:
			reversed_string += substring[::-1]
			
		else:
			reversed_string += substring[::-1]
			reversed_string += '.'


	print (reversed_string)



'''
my_string = "This is such a cutie cat."

result = ""

len_mystring = len(my_string.split(' '))

for idx, word in enumerate(my_string.split(' ')):

	if idx == len_mystring -1:

		result += word[len(word)-2::-1]
		result += "."
		
	else:
		#result.append(word[::-1])
		#result.append(' ')
		result += word[::-1]
		result += " "
		

print str(result)

# output: sihT si hcus a eituc tac.

'''
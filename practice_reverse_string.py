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
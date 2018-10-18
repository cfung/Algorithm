'''
you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Mistakes:
#1: did not realize input is a string of numbers 
#2: did not realize numbers are separated by whitespace
#3: was going thru the string directly, resulting num = 3, num = 4, instead of 34
#4: was using if num != str_space (str_space = " ")

'''
def high_and_low(numbers):
    # ...
    results = ""
    str_space = " "
    lowest = 0
    highest = 0
    numbers_list = numbers.split()
    for num in numbers_list:
        print ("num: ", num)
        #if num != str_space:
        if int(num) < lowest:
            lowest = int(num)
        if int(num) > highest:
            highest = int(num)
    results = str(highest) + " " + str(lowest)       
    return results

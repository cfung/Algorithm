import sys


a, b = [int(value) for value in sys.stdin.readline().strip().split(" ")]

print a + b

'''  my original solution

def compute_sum(a, b):
    # Write your solution here

    # This method will be called like that:

    # compute_sum(500, -5)

    if (a >= -1000 and a <= 1000) and (b >= -1000 and b <= 1000):
        return a + b
'''

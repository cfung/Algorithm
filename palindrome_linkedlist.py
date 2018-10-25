
# Question: Given a singly linked list, determine if it is a palindrome.
# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
mistake 1:  tried to use stack
mistake 2:  when for looping, forgot to use enumerate
mistake 3:  did not get the reverse idx right when looping
mistake 4:  incorrectly used while(node.next), what if node is None

'''

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mylist = []
        while (head):
            mylist.append(head.val)
            if head.next:
                #print ("head before..", head.val)
                head = head.next
                #print ("what is head now..", head.val)
            else:
                break
        for idx, item in enumerate(mylist):
            #print ("idx", idx)
            #print ("reverse: ", len(mylist)-idx)
            if item == mylist[len(mylist)-idx-1]:
                continue
            else:
                return False
        return True

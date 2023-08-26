# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#question link https://leetcode.com/problems/add-two-numbers/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions
# key is to have a dummy node and make sure you have a carry counted
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next

        return dummy.next

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 and l2:
            temp = ListNode()
            temp.val = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val + carry)//10
            tail.next = temp
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        while l1 and not l2:
            temp = ListNode()
            temp.val = (l1.val + carry)%10
            carry = (l1.val + carry)//10
            tail.next = temp
            tail = tail.next
            l1 = l1.next
        while l2 and not l1:
            temp = ListNode()
            temp.val = (l2.val + carry)%10
            carry = (l2.val + carry)//10
            tail.next = temp
            tail = tail.next
            l2 = l2.next
        while carry != 0:
            temp = ListNode()
            temp.val = carry%10
            carry = carry//10
            tail.next = temp
            tail = tail.next
        return dummy.next
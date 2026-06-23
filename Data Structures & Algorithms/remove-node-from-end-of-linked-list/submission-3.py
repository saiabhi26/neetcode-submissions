# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            l+=1
            temp = temp.next
        n = l-n
        if n == 0:
            return head.next
        temp = head
        cnt = 0
        while True:
            cnt+=1
            if cnt == n:
                temp.next = temp.next.next
                break
            temp=temp.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # prev: null, curr = head
        
        while curr: # while curr is not null
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        
        ''' First Trial : 6/17/26 
        잘한 점 : 아이디어 자체는 맞음
        아쉬운 점: 하지만 구현 방식이 틀림 : didn't think of using two pointers
        curr = head.next
        while curr.next.next != null:
            head.next = curr.next

            cur
        curr.next = head
        head.next = null
        '''
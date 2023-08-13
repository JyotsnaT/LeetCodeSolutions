'''
Author : Jyotsna
This function implements solution for reordering a list into odd nodes followed by even nodes
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        oddHead = head
        evenHead = head.next

        tempOdd = oddHead
        tempEven = evenHead

        while(tempOdd.next and tempEven.next):
            # print("odd node", tempOdd)
            # print("even node", tempEven)
            tempOdd.next = tempEven.next
            tempOdd = tempOdd.next
            
            if tempOdd.next:
                tempEven.next = tempOdd.next
                tempEven = tempEven.next
        
        # print(evenHead)
        # print(oddHead)
        # print(tempOdd)
        tempEven.next = None
        tempOdd.next = evenHead
        # print(tempOdd)
        # print(oddHead)
        return oddHead 

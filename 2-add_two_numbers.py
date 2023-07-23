# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
##beats 45% speed, 32% memory
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10
            out.append(val)
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry
            carry = val // 10
            val = val % 10
            out.append(val)
            l1 = l1.next
        while l2:
            val = l2.val + carry
            carry = val // 10
            val = val % 10
            out.append(val)
            l2 = l2.next
        if carry:
            out.append(carry)
        current_node = None
        head_node = None
        while out:
            #current node becomes head node
            #head node becomes next
            val = out.pop()
            if not current_node:
                head_node = ListNode(val)
                current_node = ListNode(val)
            else:
                current_node = head_node
                head_node = ListNode(val,current_node)
        return head_node

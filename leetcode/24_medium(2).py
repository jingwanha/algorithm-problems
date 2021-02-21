# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head

            return p
        return head

if __name__=='__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))

    sol = Solution()
    res = sol.swapPairs(head)

    while res:
        print (res.val, end=' ')
        res = res.next

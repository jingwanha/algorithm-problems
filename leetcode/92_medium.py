# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        reversed_list = ListNode(None)
        res = reversed_list

        # m번째 까지 값 할당
        for _ in range(m - 1):
            reversed_list.next = ListNode(head.val)
            reversed_list = reversed_list.next
            head = head.next

        # reverse node 계산 및 연결
        rev_node = None
        for _ in range(n - m + 1):
            rev_node, rev_node.next, head = head, rev_node, head.next
        reversed_list.next = rev_node

        # 나머지 노드 연결
        if head :
            while reversed_list.next:
                reversed_list = reversed_list.next

            while head:
                reversed_list.next = ListNode(head.val)
                reversed_list = reversed_list.next
                head = head.next


        return res.next

if __name__=='__main__':

    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    m, n = 1, 2

    sol = Solution()
    res = sol.reverseBetween(head,m,n)

    while res:
        print(res.val)
        res = res.next
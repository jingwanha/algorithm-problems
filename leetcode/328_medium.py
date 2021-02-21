# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The program should run in O(1) space complexity and O(nodes) time complexity.
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 입력이 None인 경우
        if head is None :return None

        # 초기화
        odd, even = head, head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 노드 연결
        odd.next = even_head

        return head


if __name__=='__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

    sol = Solution()
    res = sol.oddEvenList(head)

    # while res:
    #     print (res.val)
    #     res = res.next
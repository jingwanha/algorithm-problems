# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None

        # 입력 받은 리스트를 하나 씩 순회하면서
        # result linkedlist에 역순으로 저장
        while head:
            result, result.next, head = head, result, head.next

        return result

if __name__=='__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

    sol = Solution()
    res = sol.reverseList(head)

    while res:
        print (res.val)
        res = res.next


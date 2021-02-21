# https://leetcode.com/problems/palindrome-linked-list/

from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # 리스트 자료형 보다 deque 자료형을 사용하는 것이 수행시간이 더 빠름
        # 리스트의 경우, 첫 번째 요소를 pop하면 나머지 뒤 요소들에 대한 Shifting이 일어나므로 수행시간은 O(n)
        q = deque()

        if not head : return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:

            if q.popleft() != q.pop() : return False

        return True

if __name__=='__main__':
    linked_list = ListNode(1, ListNode(2,ListNode(2,ListNode(1))))

    sol = Solution()
    print (sol.isPalindrome(linked_list))
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Runner를 이용한 풀이

        reverse = None
        slow = fast = head

        # 역순으로 list 저장
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        # 입력된 링크드 리스트의 연결 숫자가 홀수인 경우
        if fast:
            slow  = slow.next

        # Palindrome 확인
        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next

        # reverse에 요쇼가 남아 있는 경우 Palindrome이 안됨
        return not reverse

if __name__=='__main__':
    linked_list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

    sol = Solution()
    print (sol.isPalindrome(linked_list))


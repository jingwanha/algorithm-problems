# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1_str, l2_str = '', ''
        result_linked_list = None

        # linked list를 문자열로 저장한 후 역순으로 저장
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        l1_str = l1_str[::-1]

        while l2:
            l2_str += str(l2.val)
            l2 = l2.next
        l2_str = l2_str[::-1]

        # 각 값을 더한 후 문자열을 역순으로 변환
        sum_value = str(int(l1_str) + int(l2_str))
        # sum_value = str(sum_value)[::-1]

        # 변환된 문자열을 linked-list로 변환
        prev: ListNode = None
        for v in sum_value:
            result_linked_list = ListNode(v)
            result_linked_list.next = prev
            prev = result_linked_list

        return result_linked_list

if __name__=='__main__':
    l1 = ListNode(2,ListNode(4,ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    sol = Solution()
    res = sol.addTwoNumbers(l1,l2)

    while res:
        print (res.val, end=' ')
        res = res.next









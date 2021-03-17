# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # convert linked-list to list
        values = []
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next
        # sort
        values = sorted(values)

        # convert list to linked-list
        head = None
        if values:
            head = result_node = ListNode(values[0])
            for val in values[1:]:
                result_node.next = ListNode(val)
                result_node = result_node.next

        return head


if __name__=='__main__':

    lists = [ListNode(1, ListNode(4, ListNode(5))),
             ListNode(1, ListNode(3, ListNode(4))),
             ListNode(2, ListNode(6))]

    sol = Solution()
    result = sol.mergeKLists(lists)

    while result:
        print(result.val, end= ' ')
        result = result.next
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        # The number of nodes in the list is in the range[0, 100].
        # 입력 리스트가 None인 경우 그대로 리턴
        if head is None: return head

        # 각 linked 리스트를 순회하면서 값을 두 개씩 저장
        swap_pylist = []
        while head and head.next:
            val1, val2 = head.val, head.next.val
            head = head.next.next

            swap_pylist.append(val2)
            swap_pylist.append(val1)

        # 홀수 개의 요소가 입력 된 경우 마지막 value 추가
        if head: swap_pylist.append(head.val)

        # pylist를 역순으로 변경 후 linked list로 변환
        swap_pylist = swap_pylist[::-1]
        prev = None

        for val in swap_pylist:
            swap_lnlist = ListNode(val)
            swap_lnlist.next = prev
            prev = swap_lnlist

        return swap_lnlist


if __name__ =='__main__':
    # head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    head = None

    sol = Solution()
    res = sol.swapPairs(head)

    while res:
        print (res.val, end=' ')
        res = res.next


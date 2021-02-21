class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 입력이 None인 경우
        if l1 == None : return l2
        elif l2 == None : return l1

        merged_list = []
        # 두 리스트의 값을 비교하여 작은 값 부터 merged_list에 저장
        while l1 and l2 :
            if l1.val == l2.val :
                merged_list.append(l1.val)
                merged_list.append(l2.val)
                l1, l2 = l1.next, l2.next

            elif l1.val > l2.val :
                merged_list.append(l2.val)
                l2 = l2.next

            elif l1.val < l2.val :
                merged_list.append(l1.val)
                l1 = l1.next

        # 나머지 index 저장
        if l1:
            while l1:
                merged_list.append(l1.val)
                l1 = l1.next
        elif l2:
            while l2:
                merged_list.append(l2.val)
                l2 = l2.next

        # merged_list를 linked list로 변경
        merged_Linked_list = None
        for i in range(len(merged_list)):
            merged_Linked_list, merged_Linked_list.next = ListNode(merged_list[-(i+1)]), merged_Linked_list

        return merged_Linked_list

if __name__=='__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    # l1 = ListNode(2)
    # l2 = ListNode(1)

    sol = Solution()
    res = sol.mergeTwoLists(l1,l2)

    while res:
        print (res.val ,end =' ')
        res = res.next


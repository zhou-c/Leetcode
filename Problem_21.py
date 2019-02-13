# 21. Merge Two Sorted Lists
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1

        #定义头结点
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        l3 = head

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return head
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
l1 = node1
l1.next = node2
node2.next = node3
node_1 = ListNode(1)
node_2 = ListNode(3)
node_3 = ListNode(4)
l2 = node_1
l2.next = node_2
node_2.next = node_3
a = Solution()
l3 = a.mergeTwoLists(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next

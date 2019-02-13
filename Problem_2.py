#2. Add Two Numbers
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        j = 0
        num1 = 0
        num2 = 0
        while l1 != None:
            num1 += l1.val * pow(10, i)
            i += 1
            l1 = l1.next
        while l2 != None:
            num2 += l2.val * pow(10, j)
            j += 1
            l2 = l2.next
        num = num1 + num2
        head = ListNode(num % 10)
        l3 = head
        num = num // 10
        while num >= 10:
            l3.next = ListNode(num % 10)
            num = num // 10
            l3 = l3.next
        if num != 0:
            l3.next = ListNode(num)
        return  head
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
l1 = node1
l1.next = node2
node2.next = node3
node_1 = ListNode(5)
node_2 = ListNode(6)
node_3 = ListNode(6)
l2 = node_1
l2.next = node_2
node_2.next = node_3
a = Solution()
l3= a.addTwoNumbers(l1, l2)
while l3 != None:
    print(l3.val)
    l3 = l3.next
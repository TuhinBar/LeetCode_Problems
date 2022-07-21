# LeetCode : (92) Reverse Linked List II (medium)
# Linked List defination:(just for testing in VS code)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Answer starts here:
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        # Check if the list is empty
        if not head:
            return None
        
        # Setting up two pointers, one for the head and one for the tail
        slowPtr,fastPtr=head,head
        # If each pointer finds it destined position, then stop will be true and backtracking for swapping will be done
        stop = False
        # Recursive function to reverse the linked list
        def recurseRev(self,fastPtr,left,right):
            # Global variable stop and slowPtr are used to control the backtracking
            nonlocal slowPtr , stop
            # Base case to stop the recursion
            if right == 1:
                return
            fastPtr = fastPtr.next
            # Moving both pointers to destined position (left and right)
            if left > 1:
                slowPtr = slowPtr.next
            recurseRev(self,fastPtr,left-1,right-1)
            # If the fast pointer reaches the end of the list, then stop is true and the backtracking is done
            if slowPtr==fastPtr or fastPtr.next == slowPtr:
                stop = True
            # Swapping the nodes while pointers are not crossing
            if not stop:
                slowPtr.val,fastPtr.val = fastPtr.val,slowPtr.val
                slowPtr = slowPtr.next
        recurseRev(self,fastPtr,left,right)
        return head

        
# Driver code

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
left = 2
right = 4

print(Solution().reverseBetween(head, left, right))
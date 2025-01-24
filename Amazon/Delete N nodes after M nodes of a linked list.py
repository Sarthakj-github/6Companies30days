'''
Given a linked list, delete n nodes after skipping m nodes of a linked list until the last of the linked list.
'''

class Solution:
    def linkdelete(self, head, n, m):
        # Code here
        prev,temp=None,head
        while temp!=None:
            for _ in range(m):
                prev,temp=temp,temp.next
                if temp==None:
                    return head
            for _ in range(n):
                temp=temp.next
                if temp==None:
                    break
            if prev==None:
                head=temp
            else:
                prev.next=temp
        return head

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new={}
        curr=head
        while curr:
            old_to_new[curr]=Node(curr.val)
            curr=curr.next
        cur=head
        while cur:
            copy=old_to_new[cur]
            copy.next=old_to_new.get(cur.next)
            copy.random=old_to_new.get(cur.random)
            cur=cur.next
        return old_to_new.get(head)
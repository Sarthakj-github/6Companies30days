'''
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
Each minute, a node becomes infected if:
The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
'''

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        d={}
        nstart=None
        def trav(p,root):
            nonlocal nstart
            if root:
                d[root]=p
                if root.val==start:
                    nstart=root
                trav(root,root.left)
                trav(root,root.right)
        trav(None,root)
        Q=[(nstart,0)]
        ans=0
        s=set((None,))
        while Q!=[]:
            a,b=Q.pop(0)
            ans=b
            s.add(a)
            if d[a] not in s:
                Q.append((d[a],b+1))
            if a.left not in s:
                Q.append((a.left,b+1))
            if a.right not in s:
                Q.append((a.right,b+1))
            
        return ans        

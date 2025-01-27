'''
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
Return the number of good leaf node pairs in the tree.
'''

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        Q=[]
        par={}
        def trav(root,pr):
            par[root]=pr
            if root.left==root.right==None:
                Q.append(root)
                return
            if root.left:
                trav(root.left,root)
            if root.right:
                trav(root.right,root)
        trav(root,None)

        c=0
        def leaf_to_leaf(root,vis,d):
            nonlocal c
            if 0<d<=distance and root.left==root.right==None:
                c+=1
            if d==distance:
                return
            vis.add(root)
            d+=1
            if root.left and root.left not in vis:
                leaf_to_leaf(root.left,vis,d)
            if root.right and root.right not in vis:
                leaf_to_leaf(root.right,vis,d)
            if par[root] and par[root] not in vis:
                leaf_to_leaf(par[root],vis,d)
        
        for root in Q:
            leaf_to_leaf(root,set(),0)

        return c//2

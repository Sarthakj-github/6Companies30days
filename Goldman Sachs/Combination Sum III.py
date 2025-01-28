'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=set()
        def trav(st,p,s,k):
            if n==s:
                if k==0:
                    ans.add(tuple(st))
                return
            if k==0:
                return
            for i in range(p+1,10):
                if i not in st:
                    st.add(i)
                    trav(st,i,s+i,k-1)
                    st.remove(i)
        trav(set(),0,0,k)
        A=[]
        for t in ans:
            A.append(list(t))
        return A

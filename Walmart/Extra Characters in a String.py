'''
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.
Return the minimum number of extra characters left over if you break up s optimally.
'''

class TrieNode:
    def __init__(self):
        self.d={}
        self.end=False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        Trie = self.make_trie(dictionary)
        return self.trav(0,s,len(s),Trie,{})
    
    def make_trie(self,dictionary):
        root=TrieNode()
        for word in dictionary:
            self.make_node(root,word)
        return root
    
    def make_node(self,temp,word):
        for l in word:
            if l not in temp.d:
                temp.d[l]=TrieNode()
            temp=temp.d[l]
        temp.end=True

    def trav(self,i,s,n,root,dp):
        if i==n:
            return 0
        if i in dp:
            return dp[i]
        temp=root
        ans=[]
        j=i
        while i<n:
            if s[i] in temp.d:
                temp=temp.d[s[i]]
            else:
                break
            i+=1
            if temp.end:
                ans.append(i)
        res=1+self.trav(j+1,s,n,root,dp)
        while ans:
            res = min(res,self.trav(ans.pop(),s,n,root,dp))
        dp[j]=res
        return dp[j]

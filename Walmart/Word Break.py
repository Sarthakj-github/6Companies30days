'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        n=len(s)
        d={}
        def trav(i):
            if i==n:
                return True
            for j in range(i+1,n+1):
                if s[i:j] in wordDict:
                    if j not in d:
                        d[j]=trav(j)
                    if d[j]:
                        return True
            return False
        return trav(0)

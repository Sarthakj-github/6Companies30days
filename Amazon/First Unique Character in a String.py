'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        d={}
        for i in range(n):
            if s[i] not in d:
                d[s[i]]=i
            else:
                d[s[i]]=-1
        for i in s:
            if d[i]!=-1:
                return d[i]
        return -1

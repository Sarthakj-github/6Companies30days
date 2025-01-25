'''
You are given two strings s and t of the same length and an integer maxCost.
You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        n=len(s)
        i,j,p,m,ans=0,0,0,0,0
        while i<n:
            k=abs(ord(s[i])-ord(t[i]))
            m+=k
            while m>maxCost and j<=i:
                m-=abs(ord(s[j])-ord(t[j]))
                j+=1
            i+=1
            ans=max(ans,i-j)
        return ans

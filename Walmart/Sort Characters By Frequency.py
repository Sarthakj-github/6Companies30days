'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        L=d.values()
        
        m=max(L)
        
        K=[]
        for i in range(m+1):
            K.append([])
        
        for i in "0123456789":
            if i in d:
                K[d[i]].append(i)
        
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i in d:
                K[d[i]].append(i)
        
        for i in "qwertyuiopasdfghjklzxcvbnm":
            if i in d:
                K[d[i]].append(i)
        
        ns=''
        for i in range(m,0,-1):
            for j in K[i]:
                ns+=j*i
        
        return ns

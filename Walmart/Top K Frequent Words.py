'''
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        l=len(words)
        L={}
        for i in words:
            if i in L:
                L[i]+=1
            else:
                L[i]=1

        r=[]
        for i in range(l,0,-1):
            if k<=0:
                break
            d=[]
            c=0
            for j in L:
                if L[j]==i:
                    d.append(j)
                    c+=1

            r+=sorted(d)[:k]
            k-=c

        return r

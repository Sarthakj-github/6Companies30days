'''
Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.
'''

class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        # code here
        n=len(arr)
        k-=1
        S=[]
        ans=[]
        for i in range(n):
            while S!=[] and arr[i]>=arr[S[-1]]:
                S.pop()
            S.append(i)
            if i>=k:
                ans.append(arr[S[0]])
            if (i-S[0])==k:
                S.pop(0)
        return ans

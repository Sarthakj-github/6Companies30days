'''
You may recall that an array arr is a mountain array if and only if:
arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
'''

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)-1
        m=10001
        i,j=1,n-1
        while i<n and j>0:
            a,b,c,d=arr[i-1]%m,arr[i]%m,arr[j]%m,arr[j+1]%m
            if a<b:
                arr[i]+=m+(arr[i-1]-a)
            if c>d:
                arr[j]+=m+(arr[j+1]-d)
            i+=1
            j-=1

        ans=0
        for i in range(1,n):
            a,b,c=arr[i-1]%m,arr[i]%m,arr[i+1]%m
            if a<b>c:
                ans=max(ans,arr[i]//m+1)
        
        if ans<3:
            ans=0
        return ans

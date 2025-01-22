'''
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d={}
        n=len(nums)
        k-=1
        s,m=0,0
        for i in range(n):
            num=nums[i]
            if num not in d:
                d[num]=0
            d[num]+=1
            s+=num
            if i>=k:
                if len(d)==k+1:
                    m=max(m,s)
                p=nums[i-k]
                s-=p
                d[p]-=1
                if d[p]==0:
                    del d[p]
        return m

'''
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i,j,n=0,0,len(nums)
        d={}
        m=0
        while j<n:
            if nums[j] not in d:
                d[nums[j]]=1
            else:
                if d[nums[j]]==k:
                    while nums[i]!=nums[j]:
                        d[nums[i]]-=1
                        i+=1
                    i+=1
                else:
                    d[nums[j]]+=1
            j+=1
            m=max(m,j-i)

        return m

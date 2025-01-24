'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        n=len(nums)
        H=[]
        for i in range(n):
            if len(H)<k:
                heappush(H,(nums[i],i))
            else:
                heappushpop(H,(nums[i],i))
        
        H.sort(key=lambda x: x[1])

        return [x for x,_ in H]

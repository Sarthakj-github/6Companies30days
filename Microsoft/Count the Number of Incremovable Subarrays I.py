'''
You are given a 0-indexed array of positive integers nums.
A subarray of nums is called incremovable if nums becomes strictly increasing on removing the subarray. For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7] because removing this subarray changes the array [5, 3, 4, 6, 7] to [5, 6, 7] which is strictly increasing.
Return the total number of incremovable subarrays of nums.
Note that an empty array is considered strictly increasing.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n=len(nums)
        A,B=[False for _ in range(n)],[False for _ in range(n)]
        A[0],B[-1]=True,True
        i=1
        while i<n and nums[i-1]<nums[i]:
            A[i]=True
            i+=1
        i=n-2
        while i>=0 and nums[i]<nums[i+1]:
            B[i]=True
            i-=1
        
        print(A,B)

        ans=0
        for i in range(n):
            for j in range(i,n):
                a,b=(0 if i==0 else nums[i-1]),(51 if j==(n-1) else nums[j+1])
                if a<b and (i==0 or A[i-1]) and (j==(n-1) or B[j+1]):
                    ans+=1
        return ans
        

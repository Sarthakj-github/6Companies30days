'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
'''

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        S=[]
        for i in range(n):
            if nums[i]%2:
                S.append(i)
        
        i,j=0,k-1
        ans=0
        print(S)
        while j<len(S):
            a,b=(-1 if i==0 else S[i-1]),(n if j==(len(S)-1) else S[j+1])
            ans+=((S[i]-a)*(b-S[j]))
            i+=1
            j+=1
        return ans

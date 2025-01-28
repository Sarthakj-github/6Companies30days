'''
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
'''

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        n1,n2=len(arr1),len(arr2)
        i,j,ans=0,0,0
        while i<n1 and j<n2:
            a,b=arr1[i]-d,arr1[i]+d
            if arr2[j]<a:
                j+=1
            else:
                if b<arr2[j]:
                    ans+=1
                i+=1
        return n1-i+ans

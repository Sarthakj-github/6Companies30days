'''
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.
Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.
Return the total number of friend requests made.
'''

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n=len(ages)
        res=0
        k=n-1
        while k>0:
            i,j,t=0,k-1,0.5*ages[k]+7
            ans=k
            while i<=j:
                m=(i+j)//2
                if ages[m]<=t:
                    i=m+1
                else:
                    ans=m
                    j=m-1
            p=k-1
            while p>=0 and ages[p]==ages[k]:
                p-=1
            res+=(k-ans)*(k-p)
            k=p
        return res

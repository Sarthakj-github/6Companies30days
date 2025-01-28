'''
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.
You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.
Implement the KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        L=[]
        heapify(L)
        n,i=len(nums),0
        while i<n:
            if i<k:
                heappush(L,nums[i])
            elif nums[i]>=L[0]:
                heappop(L)
                heappush(L,nums[i])
            i+=1
        self.k=k
        self.n=min(k,n)
        self.L=L

    def add(self, val: int) -> int:
        if self.n==self.k:
            if val>=self.L[0]:
                heappop(self.L)
                heappush(self.L,val)
        else:
            heappush(self.L,val)
            self.n+=1
        return self.L[0]

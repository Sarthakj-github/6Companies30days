'''
You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.
Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.
Note that an integer point is a point that has integer coordinates.
Implement the Solution class:
Solution(int[][] rects) Initializes the object with the given rectangles rects.
int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.
'''

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects=rects
        self.n=len(rects)
        P=[0]
        for x1,y1,x2,y2 in rects:
            P.append((x2-x1+1)*(y2-y1+1)+P[-1])
        self.P=P[1:]
    
    def pick(self) -> List[int]:
        c=random.randint(1,self.P[-1])
        i,j,ans=0,self.n-1,None
        while i<=j:
            m=(i+j)//2
            if c<=self.P[m]:
                ans=m
                if c==self.P[m]:
                    break
                j=m-1
            else:
                i=m+1
        x1,y1,x2,y2=self.rects[ans]
        return [randint(x1,x2),randint(y1,y2)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

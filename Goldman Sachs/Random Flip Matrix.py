'''
There is an m x n binary grid matrix with all the values set 0 initially. Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely to be returned.
Optimize your algorithm to minimize the number of calls made to the built-in random function of your language and optimize the time and space complexity.
Implement the Solution class:
Solution(int m, int n) Initializes the object with the size of the binary matrix m and n.
int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j] == 0 and flips it to 1.
void reset() Resets all the values of the matrix to be 0.
'''

class Solution:

    def __init__(self, m: int, n: int):
        self.flipped=set()
        self.m=m
        self.n=n

    def flip(self) -> List[int]:
        l=self.m*self.n
        while True:
            p=randrange(l)
            x,y=p//self.n,p%self.n
            if (x,y) not in self.flipped:
                self.flipped.add((x,y))
                return [x,y]

    def reset(self) -> None:
        self.flipped=set()

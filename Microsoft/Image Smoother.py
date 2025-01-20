'''
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.
'''

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n=len(img),len(img[0])
        ans=[[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                L=[(i,j),(i,j-1),(i,j+1),
                (i-1,j),(i-1,j-1),(i-1,j+1),
                (i+1,j),(i+1,j-1),(i+1,j+1)]
                s,c=0,0
                for a,b in L:
                    if 0<=a<m and 0<=b<n:
                        s+=img[a][b]
                        c+=1
                ans[i][j]=(s//c)
        return ans

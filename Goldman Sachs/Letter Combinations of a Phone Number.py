'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n=len(digits)
        ans=[]
        def trav(i,L,n):
            if i==n:
                if L!=[]:
                    ans.append(''.join(L))
                return
            if digits[i] in d:
                for j in d[digits[i]]:
                    L.append(j)
                    trav(i+1,L,n)
                    L.pop()
        trav(0,[],n)
        return ans

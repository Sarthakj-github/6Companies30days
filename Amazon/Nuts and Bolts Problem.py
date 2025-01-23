'''
Given a set of n nuts & bolts. There is a one-on-one mapping between nuts and bolts. You have to Match nuts and bolts efficiently. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means the nut can only be compared with the bolt and the bolt can only be compared with the nut to see which one is bigger/smaller.
The elements should follow the following order: { !,#,$,%,&,*,?,@,^ }
Note: Make all the required changes directly in the given arrays, output will be handled by the driver code.
'''

class Solution:

    def matchPairs(self, n, nuts, bolts):
        # code here
        
        order="!#$%&*?@^"
        k=0
        for char in order:
            for i in range(k,n):
                if char==nuts[i]:
                    nuts[i],nuts[k]=nuts[k],nuts[i]
                    bolts[k]=char
                    k+=1
                    break

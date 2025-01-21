'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        ans=set()
        if n<10:
            return []
        i=0
        j=9
        st=set()
        while j<n:
            k=s[i:j+1]
            if k in st:
                ans.add(k)
            else:
                st.add(k)
            j+=1
            i+=1
        return list(ans)

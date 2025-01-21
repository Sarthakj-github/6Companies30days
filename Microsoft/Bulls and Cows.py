'''
You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n=len(secret)
        b=0
        s,g={},{}
        for i in range(n):
            if secret[i]==guess[i]:
                b+=1
            else:
                if secret[i] not in s:
                    s[secret[i]]=0
                if guess[i] not in g:
                    g[guess[i]]=0
                s[secret[i]]+=1
                g[guess[i]]+=1
        
        c=0
        for i in s:
            if i in g:
                c+=min(s[i],g[i])
        
        return f"{b}A{c}B"

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set(['a','e','i','o','u'])
        c = 0
        maxC = 0
        for i in range(len(s)):
            if i<k:
                if s[i] in v:
                    c+=1
            else:
                if s[i] in v:
                    c+=1
                if s[i-k] in v:
                    c-=1
            maxC = max(maxC,c)
        return maxC

'''
Key concepts of the problem include:
1. Finding the largest window of vowels.
'''

'''
Improvements/simplificaitons:
1. Could have avoided using the set all together (using a string) and 
    just check if s[i] in 'aeiou': for both cases...
2. Could have checked s[i] in v first which would simplify the amount of code used.
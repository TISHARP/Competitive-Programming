class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        z = 0
        for i in t:
            if s[z]==i:
                z+=1
                if z==len(s):
                    return True
        return False
'''
Key takeaways this problem will help you understand key concepts of a subsequence:
1. we can just loop through all values in s and check if they are equal to a value in t
    if they aren't equal to that value let's continue going in t until we find a value.
    If at any point we have matched all characters of s to a character in t then it is a subsequence
    Otherwise it isn't.
2. We have to watch for the edge case of an empty string.
'''
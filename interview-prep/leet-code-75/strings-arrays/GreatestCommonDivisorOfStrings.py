from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # edge case they don't have substring that multiplies.
        if str1+str2 != str2+str1: # strings must be the same if multiplies -> order doesn't matter.
            return ""
        # return the substring that is a greatest common denominator of both string lengths
        return str[:gcd(len(str1), len(str2))]

'''
Key ideas about this problem are:
1. It wants to you get factors of both strings to compare
2. Best way to do that is with greatest common denominator
3. Edge case is that the things don't actually have a substring that multiplies.
'''
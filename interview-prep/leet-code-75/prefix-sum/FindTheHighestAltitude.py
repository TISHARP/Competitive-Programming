class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxA = 0
        curA = 0
        for i in gain:
            curA+=i
            maxA=max(curA,maxA)
        return maxA

'''
Key ideas of this problem include:
1. Use a prefix sum to keep track of the altitude we are at.
2. Return the max altitude ever reached.
'''
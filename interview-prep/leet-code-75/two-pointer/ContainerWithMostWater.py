class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxA = 0
        while l < r:
            maxA = max(maxA,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxA

'''
Key ideas of this problem:
1. Greedly check the height from on end to the other
2. Return the maximum area acheived.
'''
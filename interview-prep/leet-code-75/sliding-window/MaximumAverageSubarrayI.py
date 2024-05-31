class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxV = sum(nums[0:k])
        v = maxV
        for i in range(k,len(nums)):
            v+=nums[i]
            v-=nums[i-k]
            maxV = max(maxV,v)
        return maxV/k
        
'''
Key ideas of this problem include:
1. Sliding window technique.
2. Finding the max window and returning it divided by k to get the average.
'''
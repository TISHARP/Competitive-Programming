class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        def longestOnes(nums: List[int], k: int) -> int:
            z = 0
            maxO = 0
            o = 0
            l = 0
            for i in nums:
                if i==1 and z<=k:
                    o+=1
                elif i==0:
                    z+=1
                if z>k:
                    while nums[l]!=0:
                        l+=1
                        o-=1
                    z-=1
                    l+=1
                maxO = max(maxO, o+min(z,k))
            return maxO
        return longestOnes(nums, 1)-1

'''
Key concepts of this problem include:
1. Being lazy and using the previous problems function to calcuate the largest window of 1's
2. Returning that window allowing only 1 deletion and subtracting 1.
'''
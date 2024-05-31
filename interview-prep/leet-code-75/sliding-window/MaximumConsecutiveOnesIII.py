class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
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


'''
Key ideas of this problem include:
1. Finding the largest window of 1's.
2. Allowing the counting of zeros so long as that count doesn't surpass the threshold k
'''

'''
Note this problem is so similar to the previous that you could have used the same code
but instead with a set including only one character '1'.
'''
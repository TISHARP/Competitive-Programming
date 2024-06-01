class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            return 0 if 0 in nums else -1
        sumLeft = [0]
        sl = 0
        sumRight = [0]
        sr = 0
        for i in range(len(nums)-1):
            sl+=nums[i]
            sumLeft.append(sl)
            sr+=nums[len(nums)-i-1]
            sumRight.append(sr)
        for i in range(len(sumLeft)):
            if sumLeft[i]==sumRight[len(sumLeft)-i-1]:
                return i
        return -1

'''
Key ideas of this problem include:
1. Keep track of two prefix sums a left and a right
2. Use those prefix sums to cross pinpoint the correct index and return that index
3. Handle the edge case
'''
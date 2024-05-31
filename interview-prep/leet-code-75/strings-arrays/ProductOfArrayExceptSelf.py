class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1]*n
        cur = d = 1
        for i in range(n):
            arr[i]*=cur
            arr[n-1-i]*=d
            cur*=nums[i]
            d*=nums[n-1-i]
        return arr

'''
Key ideas of the problem:
1. Use a prefix sum... Yup it's that simple.
'''
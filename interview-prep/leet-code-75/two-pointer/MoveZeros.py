class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 
'''
Key Takeaways from this problem:
1. You can simply keep a lagging pointer that will find zeros.
2. You can always make a swap between that lagging pointer and the current pointer.
    This will initially be the exact same value.
    But as you go, it will piont to your zeros which you can easily push across by making that swap.
    Order will remain the same.
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        mni = None
        mnj = None
        g = None
        for i in nums:
            if g is not None and g < i: return True
            if mni is None:
                mni = i
            elif mnj is None:
                if mni < i:
                    mnj = i
                    g = mnj
                else:
                    mni = i
            elif i <= mni:
                mni = i
                mnj = None
            elif i < mnj:
                mnj = i
                g = mnj
        return False
'''
Key ideas of this problem include:
1. Greedily searching for a triplet...
2. The code above is fairly self explanitory but could be optimized.
    Basically we find three values...
    If one value is less than the previous value set we can keep that as a "trial value
    Once we have two values, we just need a third and we can return True
'''
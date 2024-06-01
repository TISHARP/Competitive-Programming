class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ret = [[],[]]
        for i in nums1:
            if i not in nums2:
                ret[0].append(i)
        for i in nums2:
            if i not in nums1:
                ret[1].append(i)
        return ret

'''
Another solution might look like:
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
'''


'''
Key ideas of this problem include:
1. Convert each array to a list and get the difference
2. Check that elements in the first list are not in the second.
3. Check that elements in the second list are not in the first.
4. Return those differences.
'''
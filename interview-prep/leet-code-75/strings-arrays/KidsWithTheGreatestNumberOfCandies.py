class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [x+extraCandies>=m for x in candies]

'''
Key ideas:
1. If they have the greatest number of candies among the group
    then that means they have the max of the group.
2. Just map over the list (or use a list comprehension to do so).
'''
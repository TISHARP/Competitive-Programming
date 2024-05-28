class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # We can zero pad both sides of the list to avoid index out of bounds
        # otherwise you'd have to mamke sure check for this.
        flowerbed.insert(0,0)
        flowerbed.append(0)
        ret = 0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                ret+=1
                flowerbed[i] = 1
        return ret>=n

'''
Key ideas of this problem include:
1. Looking behind and in front to see if a flower can be
    placed in your current position
2. Greedly taking any places that are available
3. Returning if the amount of placements i more or equal to required placements.
'''
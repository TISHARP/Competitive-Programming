class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        mem = {}
        for i in nums:
            if k-i in mem and mem[k-i]>0:
                mem[k-i]-=1
                ret+=1
                continue
            if i in mem:
                mem[i]+=1
            else:
                mem[i]=1
        return ret

'''
Key ideas of this problem include:
1. Memoize the elements in nums
2. If you come across an element such that k minus that element is in the memoized dictionary
    then you are going to delete that key from the list.
    In our case we just are using a counter. and removing one from the count.
3. Every time you come across those elements increment your operation counter
4. Return that counter.
'''
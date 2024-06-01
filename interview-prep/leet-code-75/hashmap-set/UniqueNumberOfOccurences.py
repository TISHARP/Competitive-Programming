class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mem = {}
        for i in arr:
            if i in mem:
                mem[i]+=1
            else:
                mem[i]=1
        return len(mem.values())==len(set(mem.values()))

'''
Solution might also look like this:
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(c.values())==len(set(c.values()))
'''

'''
Key ideas of this problem include:
1. Using a hashmap to count the values.
2. Make sure the count of all values is unique.
'''
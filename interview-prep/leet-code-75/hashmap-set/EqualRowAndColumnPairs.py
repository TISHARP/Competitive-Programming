class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        cols = []
        for i in range(len(grid)):
            col = tuple([row[i] for row in grid])
            cols.append(col)
        mem = {}
        for i in grid:
            a = tuple(i)
            if a in mem:
                mem[a]+=1
            else:
                mem[a]=1
        for j in cols:
            if j in mem:
                ret+=mem[j]
        return ret

'''
Key ideas of this problem include:
1. counting the row/column "pairs" (even though it can be more than 2 items)
2. Multiplying the row/column pair counts together to get the combinations.
'''
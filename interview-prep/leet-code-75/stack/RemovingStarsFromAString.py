class Solution:
    def removeStars(self, s: str) -> str:
        a = []
        for i in s:
            if i=="*":
                if len(a)>0: a.pop()
            else:
                a.append(i)
        return "".join(a)

'''
Key ideas of the problem include:
1. Going through a string and collecting characters that aren't '*'
2. Returning those joined back together in a string.
'''
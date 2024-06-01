class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        m1 = {}
        m2 = {}
        for i in range(len(word1)):
            if word1[i] in m1:
                m1[word1[i]]+=1
            else:
                m1[word1[i]]=1
            if word2[i] in m2:
                m2[word2[i]]+=1
            else:
                m2[word2[i]]=1
        c1 = list(sorted(m1.values()))
        c2 = list(sorted(m2.values()))
        for i in range(len(c1)):
            if c1[i]!=c2[i]:
                return False
        return set(m1.keys())==set(m2.keys())
'''
Another solution: provided by mak2rae: https://leetcode.com/problems/determine-if-two-strings-are-close/solutions/4565072/beats-99-python3-hash-table-easy-to-understand
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        return set(cnt1.keys()) == set(cnt2.keys()) and sorted(cnt1.values()) == sorted(cnt2.values())
'''

'''
Key ideas of this problem include:
1. Making sure that the counts of both strings numerically are the same and mapped correctly.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        w = ""
        for i in s:
            if i!=" ":
                w+=i
            elif w!="":
                ret.append(w)
                w = ""
        if w!="":
            ret.append(w)
        return " ".join(reversed(ret))

'''
Another solution:
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x for x in filter(lambda x: len(x.strip())>0, reversed(s.strip().split(" ")))])
'''

'''
Key takeaways from this problem:
1. Store words in a list and reverse and join that together...
2. You can either go character by character and determine if we are starting a new word or:
3. you can split the string, strip the components and join all of that today.
'''
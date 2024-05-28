class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        i = 0 # traversal index
        while i < len(word1) and i < len(word2): # go until one string runs out of letters.
            s+=word1[i]
            s+=word2[i]
            i+=1
        if i<len(word1): # if we ran out of word2 that means we can append the rest of word 1
            s+=word1[i:]
        else:
            s+=word2[i:] # if we ran out of word1 then we append the rest of word 2
        return s # return the result.

'''
Key ideas about this problem are:
1. It wants you to understand when an index will go out of range.
2. It wants you to be able to add add the rest of a word after such even happens.

Time Complexity
O(n)
Space Complexity
O(n) (unless you aren't counting the return string which would then be considered O(1))

Another way to solve this would be to use a for loop, and loop through the minimum length of each word.
Then after you loop through that, you can append the rest of the word by starting with the lesser length
And appending that to your return.
'''
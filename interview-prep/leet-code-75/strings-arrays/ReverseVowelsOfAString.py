class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # strings are immutable, but arrays are mutable.
        arr = [x for x in s]
        while l < r:
            # find left side vowel.
            while l < r and s[l] not in vowels:
                l+=1
            # find right side vowel.
            while r > l and s[l] in vowels and s[r] not in vowels:
                r-=1
            # we have two vowels for sure make the swap
            # the only case we wouldn't have two vowels is if r=l and swap doesn't matter.
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        # convert the array back into string.
        return "".join(arr)

'''
Key takeaways include:
1. Immutability of strings in python and a lot of other languages
    i.e. we will use an array to make swaps.
2. We can use two pointers to get the left most and right most indexes 
    and close in toward the center.
'''
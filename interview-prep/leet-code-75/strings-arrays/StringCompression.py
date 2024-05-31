class Solution:
    def compress(self, chars: List[str]) -> int:
        p = None
        c = 0
        z = 0
        i = 0
        while i < len(chars):
            if chars[i]==p:
                c+=1
                del chars[i]
            else:
                if p is not None and c>1:
                    if c >= 1000:
                        chars.insert(z+1,str(c//1000))
                        z+=1
                        i+=1
                    if c >= 100:
                        chars.insert(z+1,str((c%1000)//100))
                        z+=1
                        i+=1
                    if c >= 10:
                        chars.insert(z+1,str((c%100)//10))
                        z+=1
                        i+=1
                    chars.insert(z+1,str((c%10)))
                    i+=1
                z = i
                p = chars[i]
                i+=1
                c = 1
        if c>1:
            if c >= 1000:
                chars.insert(z+1,str(c//1000))
                z+=1
            if c >= 100:
                chars.insert(z+1,str((c%1000)//100))
                z+=1
            if c >= 10:
                chars.insert(z+1,str((c%100)//10))
                z+=1
            chars.insert(z+1,str((c%10)))
        return len(chars)
'''
Key ideas of this problem include:
1. Go through and count a character until you find another character.
2. Once that happens you will need to reduce the count back down into digits and **insert** each digit
    into the array in place.
    We can keep an extra variable z to keep track of where these are... See improvement section for
    what I'd change about this approach.
'''
'''
What I'd do to improve the code above if I was to re-write it:
1. I'd make the capturing of digits easier instead of what I've done here.
2. I'd store the result in two separate arrays to make 1. easier.
'''
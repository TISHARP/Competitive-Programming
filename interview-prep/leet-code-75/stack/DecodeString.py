class Solution:
    def decodeString(self, s: str) -> str:
        ret = ""
        stack = []
        c = 0
        for i in s:
            if i.isdigit():
                c*=10
                c+=int(i)
            elif i=="[":
                stack.append(c)
                stack.append(ret)
                c = 0
                ret = ""
            elif i=="]":
                p = stack.pop()
                n = stack.pop()
                ret = p+ret*n
            else:
                ret+=i
        while stack:
            ret=stack.pop()+ret
        return ret

'''
Key ideas of this problem include:
1. Collecting digits to create a number.
2. Adding letters and those numbers to a stack
3. Uncompressing the stack by going back through the stack and adding those values to the return
4. Returning that string.
'''
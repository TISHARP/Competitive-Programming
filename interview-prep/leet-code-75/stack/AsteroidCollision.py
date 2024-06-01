class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        ret = [a[0]]
        for i in range(1,len(a)):
            ret.append(a[i])
            while len(ret)>1 and ret[len(ret)-2]>0 and ret[len(ret)-1]<0: #collision
                if abs(ret[len(ret)-2])>abs(ret[len(ret)-1]): #destroy negetive asteroid
                    ret.pop()
                elif ret[len(ret)-2]*-1==ret[len(ret)-1]: #destroy both asteroids
                    ret.pop()
                    ret.pop()
                else: #destroy positive asteroid
                    del ret[len(ret)-2]
        return ret

'''
Key ideas of the problem include:
1. Finding where a collision occurs.
2. A collision only ever occurs if an asteroid is going right and the other is going left.
'''
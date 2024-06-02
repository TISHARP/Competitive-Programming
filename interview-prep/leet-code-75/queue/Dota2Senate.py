class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = br = 0
        d = bd = 0
        a = [x for x in senate]
        z = len(a)
        fr = False
        fd = False
        while z>1:
            i = j = 0
            m = len(a)
            if fr and not fd:
                return "Radiant"
            elif fd and not fr:
                return "Dire"
            fr = False
            fd = False
            while i < z:
                if a[i]=="R":
                    fr = True
                    #check if we have d's available
                    if bd>0:
                        bd-=1
                        del a[i]
                        i-=1
                        z-=1
                    else:
                        r+=1
                        br+=1
                else:
                    fd = True
                    if br>0:
                        br-=1
                        del a[i]
                        i-=1
                        z-=1
                    else:
                        d+=1
                        bd+=1
                i+=1
        if a[0]=="R":
            return "Radiant"
        else:
            return "Dire"

'''
Key ideas of the problem include:
1. Keeping track how how many D's or R's we have in a queue
2. Popping D's and R's from the queue as necessary.
'''
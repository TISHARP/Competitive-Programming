from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

'''
Key ideas of the problem include:
1. Keeping track of a queue that will include all values until they are outside of scope.
'''
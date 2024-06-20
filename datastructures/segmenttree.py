class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        # Initialize leaf nodes in the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the segment tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        """ Update the value at the given index to 'value' """
        # Update the leaf node
        pos = self.n + index
        self.tree[pos] = value
        # Update the segment tree by propagating the change upwards
        while pos > 1:
            pos = pos>>1
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        """ Range sum query for the range [left, right) """
        # Initialize result to identity element for sum (0)
        result = 0
        # Adjust indices to be within bounds
        left += self.n
        right += self.n
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left = left>>1
            right = right>>1 # note same thing as right = right // 2 as well as right //=2
        return result

'''
This is the basic setup for a segment tree... In this example it's a summation segment tree.
If you wanted to find mins maxes or other factors then you'd need to
first update the query and update methods. To accomodate that.
This is just a basic setup.
'''
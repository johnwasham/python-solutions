# update a value at index
# query a range L, R (for sum, etc)
# because we have the ability to update a value, we can't use prefix sum
from functools import update_wrapper


# update - log n
# query - log n

# we break into left/right halves going down the tree until you get to single index
# each node has left index, right index, and sum at that node
# get sum for a node by adding its left and right children
# all nodes have a left and right child


class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2
        if index <= M:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        self.sum = self.left.sum + self.right.sum

    def range_query(self, L, R):
        if L == self.L and R == self.R:
            return self.sum

        M = (L + R) // 2

        if L > M:
            return self.right.range_query(L, R)
        elif R <= M:
            return self.left.range_query(L, R)
        else:
            return self.left.range_query(L, M) + self.right.range_query(M + 1, R)




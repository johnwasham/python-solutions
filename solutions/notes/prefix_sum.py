# prefixes are contiguous blocks that start at the beginning

# prefix sum or prefix product
# postfix starts at end

class PrefixSum:
    def __init__(self, nums):
        self.psum = [0] * len(nums)
        total = 0

        for i, n in enumerate(nums):
            total += n
            self.psum[i] = total

    def range_sum(self, left, right):
        rsum = self.psum[right]
        return rsum - self.psum[left - 1] if left > 0 else rsum

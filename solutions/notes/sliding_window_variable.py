# Find length of the minimum size subarray where the sum is
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)

def shortestSubAray(nums, target):
    total = 0
    length = float("inf")
    L = 0

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1

    return 0 if length == float("inf") else length
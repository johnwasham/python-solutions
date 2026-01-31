# find is there are duplicates in subarray of size k

def close_duplicates(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            return True

        window.add(nums[R])

    return False

# variable size

# find length of longest subarray filled with the same value
# [4, 2, 2, 3, 3, 3]

def longest_dup_subarray(nums):
    max_len = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        max_len = max(max_len, R - L + 1)

    return max_len
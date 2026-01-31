# Find a non-empty subarray with the largest sum, return sum

def kadanes(nums):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += n
        max_sum = max(max_sum, cur_sum)

    return max_sum


# Find the indices of the subarray with the largest sum

def sliding_window(nums):
    max_sum = nums[0]
    cur_sum = 0
    max_l, max_r = 0, 0
    L = 0

    for R in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
            L = R

        cur_sum += nums[R]

        if cur_sum > max_sum:
            max_sum = cur_sum
            max_l = L
            max_r = R

    return [max_l, max_r]

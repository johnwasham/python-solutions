def is_palindrome(word):
    L, R = 0, len(word) - 1

    while L > R:
        if word[L] != word[R]:
            return False
        L +=1
        R -=1

    return True


def find_indices_for_target_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r += 1
        else:
            return [l, r]

    return None

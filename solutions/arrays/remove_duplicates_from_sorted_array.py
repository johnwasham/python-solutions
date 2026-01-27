"""
You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

Note:

The order of the unique elements should remain the same as in the original array.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain all the unique elements.
Return k as the final result.
"""

# mine

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         last = nums[0]
#         insert = 1
#         i = 1
#
#         while i < len(nums):
#             while i < len(nums) and nums[i] == last:
#                 i += 1
#
#             if i < len(nums):
#                 last = nums[i]
#                 nums[insert] = nums[i]
#                 insert += 1
#                 i += 1
#
#         return insert

# better:

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
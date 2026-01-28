"""
Sort Colors
Medium
Company Tags
You are given an array nums consisting of n elements where each element is an integer representing a color:

0 represents red
1 represents white
2 represents blue
Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

Example 1:

Input: nums = [1,0,1,2]

Output: [0,1,1,2]
Example 2:

Input: nums = [2,1,0]

Output: [0,1,2]
Constraints:

1 <= nums.length <= 300.
0 <= nums[i] <= 2.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?


"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums or len(nums) == 1:
            return

        counts = [0] * 3
        n = len(nums)

        for i in range(n):
            counts[nums[i]] += 1

        i = 0
        for j in range(len(counts)):
            for k in range(counts[j]):
                nums[i] = j
                i += 1


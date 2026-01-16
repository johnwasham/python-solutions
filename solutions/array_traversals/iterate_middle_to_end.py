"""
Our task is as follows: Given an array of integers, we aim to return a new array that emerges from the center of the original array and alternates direction towards both ends. In other words, the first element of our new array will be the middle element of the original one. After establishing the starting point, we will alternate between the elements to the left and to the right of the initial center until we have incorporated every element. If the length of the initial array is even, we first take the the element to the left of the center, then the one to the right of the center, then do the alternation as described above.

For example, for numbers = [1, 2, 3, 4, 5], the output should be [3, 2, 4, 1, 5].
"""


def iterate_middle_to_end(numbers):
    mid = len(numbers) // 2  # Middle index if odd; right-middle index if even
    if len(numbers) % 2 == 1:
        left = mid - 1  # The left to the middle element
        right = mid + 1  # The right to the middle element
        new_order = [numbers[mid]]  # Adding the middle element to the resulting array
    else:
        left = mid - 1  # Left middle element
        right = mid  # Right middle element
        new_order = []  # No elements in the resulting array for now

    while left >= 0 and right < len(numbers):
        new_order.append(numbers[left])
        new_order.append(numbers[right])
        left -= 1
        right += 1

    return new_order


assert iterate_middle_to_end([1, 2, 3, 4, 5]) == [3, 2, 4, 1, 5]

"""
You are tasked with writing a Python function to multiply two extremely large positive integers. These are not your regular-sized large numbers; they are represented as strings potentially up to 500 digits long.

Your function should take two string parameters, representing the two large integers to be multiplied, and return the product as a string. The challenging part is that you should perform the multiplication without converting the entire strings into integers.

Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.

Furthermore, bear in mind that when multiplying numbers manually, we align the numbers vertically and multiply each digit of the first number with each digit of the second number, starting from the rightmost digits, and add the results after shifting appropriately.

Please solve this problem using similar, decision-based string manipulations instead of merely converting strings into integers, multiplying them, and converting the result back to a string. This approach is imperative as direct multiplication would not be feasible for very large numbers.
"""

def solution(num1: str, num2: str) -> str:
    # Quick return for trivial cases
    if num1 == "0" or num2 == "0":
        return "0"

    # Work with reversed digit lists to make the index equal to
    # the power of ten (units at index 0).
    a_rev = [ord(ch) - 48 for ch in num1[::-1]]
    b_rev = [ord(ch) - 48 for ch in num2[::-1]]

    # Result can be at most len(a_rev)+len(b_rev) digits
    res = [0] * (len(a_rev) + len(b_rev))

    # Grade‑school multiplication
    for i, da in enumerate(a_rev):
        carry = 0
        for j, db in enumerate(b_rev):
            pos = i + j
            prod = da * db + res[pos] + carry
            res[pos] = prod % 10          # keep only one digit
            carry   = prod // 10          # propagate the rest

        if carry:
            res[i + len(b_rev)] += carry

    # Remove leading zeros
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    # Convert back to a string
    return ''.join(chr(d + 48) for d in reversed(res))



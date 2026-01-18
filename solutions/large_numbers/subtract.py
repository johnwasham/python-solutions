"""
You are given two exceedingly large positive decimal numbers, num1 and num2, both represented as strings. The length of these strings can range anywhere from 1 to 500 characters. The challenge here is to subtract num2 from num1 without directly converting the strings into integers.

Create a Python function that performs this operation and returns the resultant string, referred to as num3.

Please note that the subtraction will not result in a negative number, as num1 will always be greater than or equal to num2.
"""

def solution(num1: str, num2: str) -> str:
    """
    Subtracts two non‑negative decimal numbers represented as strings.
    Assumes num1 >= num2.  The input lengths can be up to 500 digits,
    so the operation is performed digit by digit instead of converting
    to int.

    Parameters
    ----------
    num1 : str
        The minuend (larger or equal number).
    num2 : str
        The subtrahend.

    Returns
    -------
    str
        The difference (num1 - num2) as a decimal string with no leading zeros,
        except that the single digit '0' is returned for a zero result.
    """
    # Make both strings the same length by left‑padding num2 with zeros
    n1, n2 = len(num1), len(num2)
    if n2 < n1:
        num2 = num2.rjust(n1, '0')
    elif n1 < n2:
        # This case should not happen because num1 >= num2
        raise ValueError("num1 must be greater than or equal to num2")

    carry = 0          # borrow flag (0 or 1)
    result = []

    # Process from the least significant digit to most
    for d1, d2 in zip(num1[::-1], num2[::-1]):
        digit1 = ord(d1) - 48          # int conversion without int()
        digit2 = ord(d2) - 48
        sub = digit1 - carry - digit2
        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0
        result.append(chr(sub + 48))

    # Remove any leading zeros from the most significant side
    while len(result) > 1 and result[-1] == '0':
        result.pop()

    # The result is currently reversed
    return ''.join(result[::-1])

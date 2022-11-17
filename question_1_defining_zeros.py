"""
Define zeroes(n) as the number of zeroes in the decimal expansion of the integer n.
A number n is zero_special if zeroes(n) > zeroes(n-1).

Write a function that determines whether n is zero_special.
"""


def zeroes(n):
    """
    Return the number of zeroes in the decimal expansion of n.
    """
    if n == 0:
        return 1
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count


def is_zero_special(n):
    """
    Return True if n is zero_special, False otherwise.
    """
    return zeroes(n) > zeroes(n - 1)


def test_is_zero_special():
    """
    Test is_zero_special.
    """
    assert is_zero_special(1000) == True
    assert is_zero_special(100) == True
    assert is_zero_special(10) == True
    assert is_zero_special(1) == False
    assert is_zero_special(0) == True
    assert is_zero_special(81) == False


test_is_zero_special()

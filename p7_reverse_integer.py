#! /usr/bin/env -S uv run
"""
LeetCode 7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Difficulty: Easy

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], return 0.
"""

from test_lib import run_tests

INT_MIN, INT_MAX = -(2**31), 2**31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10

        res *= sign
        return res if INT_MIN <= res <= INT_MAX else 0


if __name__ == "__main__":
    run_tests(
        [
            (Solution().reverse, (123,), 321, "basic case"),
            (Solution().reverse, (-123,), -321, "negative case"),
            (Solution().reverse, (120,), 21, "trailing zero case"),
        ]
    )

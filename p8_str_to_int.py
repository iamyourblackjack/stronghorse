#! /usr/bin/env -S uv run
"""
LeetCode 8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

Difficulty: Medium

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi
function).
"""

from test_lib import run_tests

INT_MIN, INT_MAX = -(2**31), 2**31 - 1


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] in "+-":
            sign = -1 if s[0] == "-" else 1
            i = 1

        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign
        return max(INT_MIN, min(INT_MAX, res))


if __name__ == "__main__":
    run_tests(
        [
            (Solution().myAtoi, ("42",), 42, "basic case"),
            (Solution().myAtoi, ("   -42",), -42, "negative case"),
            (Solution().myAtoi, ("4193 with words",), 4193, "words after number"),
            (Solution().myAtoi, ("-91283472332",), INT_MIN, "overflow negative"),
            (Solution().myAtoi, ("91283472332",), INT_MAX, "overflow positive"),
        ]
    )

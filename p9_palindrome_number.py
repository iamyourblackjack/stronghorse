#! /usr/bin/env -S uv run
"""
LeetCode 9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Difficulty: Easy

Given an integer x, return true if x is a palindrome, and false otherwise.
"""

from test_lib import run_tests


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    run_tests(
        [
            (Solution().isPalindrome, (121,), True, "basic case"),
            (Solution().isPalindrome, (-121,), False, "negative case"),
            (Solution().isPalindrome, (10,), False, "not a palindrome"),
        ]
    )

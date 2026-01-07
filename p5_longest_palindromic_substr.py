#! /usr/bin/env -S uv run
"""
LeetCode 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Difficulty: Medium

Given a string s, return the longest palindromic substring in s.
"""

from test_lib import run_tests


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right  # [left+1, right)

        start = end = 0

        for i in range(len(s)):
            for left, right in (expand(i, i), expand(i, i + 1)):
                if right - left > end - start:
                    start, end = left, right

        return s[start:end]


if __name__ == "__main__":
    run_tests(
        [
            (Solution().longestPalindrome, ("babad",), "bab", "basic case"),
            (Solution().longestPalindrome, ("cbbd",), "bb", "even length"),
            (Solution().longestPalindrome, ("a",), "a", "single character"),
            (Solution().longestPalindrome, ("ac",), "a", "two characters"),
        ]
    )

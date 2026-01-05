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

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r  # [l+1, r)

        start = end = 0

        for i in range(len(s)):
            for l, r in (expand(i, i), expand(i, i + 1)):
                if r - l > end - start:
                    start, end = l, r

        return s[start:end]


if __name__ == "__main__":
    run_tests([
        (Solution().longestPalindrome, ("babad",), "bab", "basic case"),
        (Solution().longestPalindrome, ("cbbd",), "bb", "even length"),
        (Solution().longestPalindrome, ("a",), "a", "single character"),
        (Solution().longestPalindrome, ("ac",), "a", "two characters"),
    ])
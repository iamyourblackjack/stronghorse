#! /usr/bin/env -S uv run
"""
LeetCode 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.
"""
from test_lib import run_tests


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window approach - O(n) time, O(min(n, m)) space
        """
        left = 0
        res = 0
        seen: dict[str, int] = {}
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            seen[ch] = right
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    run_tests([
        (Solution().lengthOfLongestSubstring, ("abcabcbb",), 3, "basic case"),
        (Solution().lengthOfLongestSubstring, ("bbbbb",), 1, "all same characters"),
        (Solution().lengthOfLongestSubstring, ("pwwkew",), 3, "contains repeating characters"),
    ])
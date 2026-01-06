#! /usr/bin/env -S uv run
"""
LeetCode 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Difficulty: Easy

Given an array of strings strs, return the longest common prefix, which is the longest string that is the prefix of all the strings in the array.
"""
from test_lib import run_tests


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix


if __name__ == "__main__":
    run_tests([
        (Solution().longestCommonPrefix, (["flower", "flow", "flight"],), "fl", "basic case"),
        (Solution().longestCommonPrefix, (["dog", "racecar", "car"],), "", "no common prefix"),
    ])
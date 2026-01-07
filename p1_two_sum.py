#!/usr/bin/env -S uv run
"""
LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
"""

from test_lib import run_tests


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Hash map approach - O(n) time, O(n) space
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    run_tests(
        [
            (two_sum, ([2, 7, 11, 15], 9), [0, 1], "basic case"),
            (two_sum, ([3, 2, 4], 6), [1, 2], "middle elements"),
            (two_sum, ([3, 3], 6), [0, 1], "same element twice"),
            (two_sum, ([-1, -2, -3, -4, -5], -8), [2, 4], "negative numbers"),
        ]
    )

#! /usr/bin/env -S uv run
"""
LeetCode 15. 3Sum
https://leetcode.com/problems/3sum/

Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""
from test_lib import run_tests


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result


if __name__ == "__main__":
    run_tests([
        (Solution().threeSum, ([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]], "basic case"),
        (Solution().threeSum, ([0, 0, 0],), [[0, 0, 0]], "all zeros"),
        (Solution().threeSum, ([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],), [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]], "multiple solutions"),
    ])
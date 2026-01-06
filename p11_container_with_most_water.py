#! /usr/bin/env -S uv run
"""
LeetCode 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Difficulty: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
"""
from test_lib import run_tests
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area: width * min height
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            
            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area


if __name__ == "__main__":
    run_tests([
        (Solution().maxArea, ([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49, "basic case"),
        (Solution().maxArea, ([1, 1],), 1, "two elements"),
        (Solution().maxArea, ([4, 3, 2, 1, 4],), 16, "max at the ends"),
        (Solution().maxArea, ([1, 2, 1],), 2, "symmetric case"),
    ])
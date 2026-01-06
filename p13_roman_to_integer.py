#! /usr/bin/env -S uv run
"""
LeetCode 13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Difficulty: Easy

Given a roman numeral, convert it to an integer.
"""
from test_lib import run_tests


class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman numeral to its value
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        # Iterate from right to left
        for char in reversed(s):
            value = roman_values[char]
            # If current value is less than previous, subtract it (e.g., IV = 5 - 1)
            # Otherwise, add it
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        
        return result


if __name__ == "__main__":
    run_tests([
        (Solution().romanToInt, ("III",), 3, "basic case"),
        (Solution().romanToInt, ("LVIII",), 58, "mixed case"),
        (Solution().romanToInt, ("MCMXCIV",), 1994, "large number"),
    ])
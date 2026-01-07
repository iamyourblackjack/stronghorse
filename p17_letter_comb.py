#! /usr/bin/env -S uv run
"""
LeetCode 17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Difficulty: Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
"""
from test_lib import run_tests
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, path: str) -> None:
            # If we've processed all digits, add the combination
            if index == len(digits):
                result.append(path)
                return
            
            # Get letters for current digit and try each one
            letters = phone_map[digits[index]]
            for letter in letters:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result

if __name__ == "__main__":
    run_tests([
        (Solution().letterCombinations, ("23",), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "basic case"),
        (Solution().letterCombinations, ("",), [], "empty input"),
        (Solution().letterCombinations, ("2",), ["a", "b", "c"], "single digit"),
        (Solution().letterCombinations, ("234",), ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"], "multiple digits"),
        (Solution().letterCombinations, ("9",), ["w", "x", "y", "z"], "single digit with multiple letters"),
        (Solution().letterCombinations, ("78",), ["pt", "pu", "pv", "qt", "qu", "qv", "rt", "ru", "rv", "st", "su", "sv"], "two digits with multiple letters"),
    ])
    
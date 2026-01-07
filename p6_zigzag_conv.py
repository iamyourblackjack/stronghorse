#! /usr/bin/env -S uv run
"""
LeetCode 6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

Difficulty: Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
"""

from test_lib import run_tests


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        strList: list[str] = [""] * numRows
        cur = 0
        step = 1  # 1 means moving down, -1 means move up

        for i in range(len(s)):
            strList[cur] += s[i]
            if cur == numRows - 1:
                step = -1
            elif cur == 0 and step != 1:
                step = 1

            cur += step

        return "".join(strList)


if __name__ == "__main__":
    run_tests(
        [
            (Solution().convert, ("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR", "basic case"),
            (Solution().convert, ("PAYPALISHIRING", 4), "PINALSIGYAHRPI", "zigzag pattern"),
            (Solution().convert, ("A", 1), "A", "single row"),
        ]
    )

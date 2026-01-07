#! /usr/bin/env -S uv run
"""
LeetCode 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Difficulty: Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
"""

from list_lib import ListNode
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def test_add_two_numbers(l1: list[int], l2: list[int], expected: list[int], name: str):
    """Wrapper to test with list inputs/outputs."""
    result = Solution().addTwoNumbers(ListNode.from_list(l1), ListNode.from_list(l2))
    result_list = result.to_list() if result else []
    status = "✓" if result_list == expected else "✗"
    print(f"  {status} {name}: {l1} + {l2} → {result_list}")
    assert result_list == expected, f"Expected {expected}, got {result_list}"


if __name__ == "__main__":
    print("Running tests...")
    test_add_two_numbers([2, 4, 3], [5, 6, 4], [7, 0, 8], "basic case")
    test_add_two_numbers([0], [0], [0], "zeros")
    test_add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1], "carry overflow")
    print("All tests passed!")

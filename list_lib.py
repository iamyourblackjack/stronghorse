from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(vals: list[int]) -> ListNode | None:
        """Convert a Python list to a linked list."""
        if not vals:
            return None
        head = ListNode(vals[0])
        curr = head
        for val in vals[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def to_list(self) -> list[int]:
        """Convert linked list to a Python list."""
        result = []
        curr: ListNode | None = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

from dataclasses import dataclass
from typing import Optional, List


BASE = 10


@dataclass
class ListNode:
    def __init__(self, val: Optional[int] = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def make_from_list(nums: List[int]) -> ListNode:
    output = ListNode()
    head = output
    for num in nums:
        head.next = ListNode(num)
        head = head.next
    return output.next


def get_answer(n1, n2, rem, base) -> int:
    return (n1 + n2 + rem) % base


def get_remainder(n1, n2, rem, base) -> int:
    return (n1 + n2 + rem) // base


def add(n1: int, n2: int, remainder: int) -> (int, int):
    global BASE
    return get_answer(n1, n2, remainder, BASE), get_remainder(n1, n2, remainder, BASE)


def add_nodes(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    output = ListNode()
    head = output

    remainder = 0
    v1, v2, v3 = 0, 0, 0

    while l1 or l2:
        if l1 is not None:
            v1 = l1.val
        else:
            v1 = 0

        if l2 is not None:
            v2 = l2.val
        else:
            v2 = 0

        v3, remainder = add(v1, v2, remainder)
        head.next = ListNode(v3)
        head = head.next

        if l1 is None:
            pass
        else:
            l1 = l1.next

        if l2 is None:
            pass
        else:
            l2 = l2.next

    if remainder > 0:
        head.next = ListNode(remainder)

    head = head.next
    return output.next


def main():
    vals1 = [9, 9, 9, 9, 9, 9, 9]
    vals2 = [9, 9, 9]

    l1 = make_from_list(vals1)
    l2 = make_from_list(vals2)

    result = add_nodes(l1, l2)

    while result:
        print(result.val)
        result = result.next


if __name__ == "__main__":
    main()

"""
#2: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Examples:

#1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explantion: 342 + 465 = 807


#2:
Input: l1 = [0], l2 = [0]
Output: [0]

#3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- 1 <= nodes <= 100
- 0 <= Node.val <= 9
- number does not have leading zeros
  - Note: leading zero is at the front of a number but our numbers are reversed. So, we could get a number like this 0 -> 0 -> 0 -> 0 -> 1 + 3 -> 1 if you didn't keep going to add everything


Thoughts
- "non-empty" implies not None, do not trust
- non-negative implies > 0
- reverse order = linked lists can begin with 0


Problem
There exists for two sequences of non-negative numbers in linked lists, a sequence that is the sum of the two provided linked lists.

Output
- base 10 modulo addition with remainder carried

Input -> Process -> Output

E #1:

1. l1.val = 2 + l2.val = 5 = 7 -> l3.val = 7 -> l1 = l1.next, l2 = l2.next
2. l1.val = 4 + l2.val = 6 = 10 -> l3.val = 10 % 10 = 0, remainder = 1


"""

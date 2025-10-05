from dataclasses import dataclass

from typing import Optional, Any, List

"""
ADD TWO NUMBERS

#medium #math #linked-lists

PROBLEM #1
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add two numbers and return the sum as the linked list.

You may assume the tow numbers do not contain any leading zero, except the number 0 itself.


EXAMPLES #1: 
    2 -> 4 -> 3
+   5 -> 6 -> 4
=   7 -> 0 -> 7 + 1 = 8
= 7 -> 0 -> 8


ENTITIES:
- Digits = Values = 0 <= Node.val <= 9 = 10 digits and we are working by position such that with each number we should think in terms of it's position in the number as well as th addition
- Base = result of modulo arithmetic = max = (9 + 9) // 10
- Remainder = 0 or 1 = the result of any operation in base 10 is either less than 10 or equal 10 or greater than 10
- Number is reversed because it is inserted on the tail like a stack such that the result is the first digit (maybe important)
- Number of nodes in linked list from 1 <= nodes <= 100
- There are no leading zeros in number to be worried about

# [x] add two values
# [x] add two values - modulo
# [x] add two nodes

"""


MOD_BASE = 10


"""
# -------- LINKED LIST DATA STRUCTURE -------
"""


@dataclass
class ListNode:
    def __init__(self, val: Optional[int] = None, next: Optional["ListNode"] = None):
        self.val: Optional[int] = val
        self.next: Optional["ListNode"] = next

    def __repr__(self):
        return self.val


@dataclass
class LinkedList:
    def __init__(self, nodes: Optional[List] = None):
        self.head = None
        self.nodes = nodes

    def __post_init__(self):
        if self.nodes is not None:
            node = ListNode(val=self.nodes.pop(0))
            self.head = node
            for elem in self.nodes:
                node.next = ListNode(val=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


def get_remainder(x: int, base: int = 10) -> int:
    return x % base


def convert_to_base(x: int, base: int = 10) -> int:
    return x // base


def add_(x: int, y: int) -> int:
    return x + y


def add(x: Optional[int] = None, y: Optional[int] = None) -> int:
    if not x:
        x = 0

    if not y:
        y = 0
    return add_(x, y)


def modulo_add(x: Optional[int], y: Optional[int]) -> int:
    return convert_to_base(add(x, y), 10)


def main():
    vals1 = [2, 4, 3]
    ll1 = LinkedList(vals1)
    print(ll1)
    for l1 in ll1:
        print(l1)


if __name__ == "__main__":
    main()

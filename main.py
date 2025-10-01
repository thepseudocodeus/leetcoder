from typing import Optional
from dataclasses import dataclass

@dataclass
class ListNode:
    def __init__(self, val: Optional[int] = 0, next: Optional["ListNode"] = None):
        self.val: Optional[int] = None
        self.next: Optional["ListNode"] = None

@dataclass
class LinkedList:
    def __init__(self, node: Optional[ListNode] = None):
        self.head = node
        self.tail = None

def check_invariants(L1, L2, L3):
    # - [] Invariant 1: L3 length should = length of L1 + L2
    assert len(L3) == len(L1) + len(L2), "Length mismatch"

    # - [] Invariant 2: L3 should be in nondescending order
    assert all(L3[i] <= L3[i+1] for i in range(len(L3))), "Order violated"

    # - [] Invariant 3: elements preserved
    combined = sorted(L1 + L2)
    assert L3 == combined, "Elements preserved"

    return True


def new_node(value: int) -> ListNode:
    return ListNode(val=value)

def connect_nodes(left: ListNode, right: ListNode) -> ListNode:
    left.next = right
    return left


def new_nodes(*values) -> ListNode:
    output = ListNode()
    assert output is not None, f"Expect node is not None: {output}"
    for val in values:
        if not output:
            output.val = val
        output.next = ListNode(val)
    return output


def print_list_recursively(node: Optional[ListNode] = None):
    if node is None:
        return

    assert node is not None, "Node should never be None"
    
    value = node.val
    assert value is not None, f"Nodes should all have values. Got the following: {value}"
    print(f"Printing node. Current Value = {value}")

    print("Recursing back through function")
    print_list_recursively(node.next)


def new_linked_list_recursive(numbers: Optional[List[int]] = None) -> ListNode:
    # [ ] TODO: When should we exit for sure?
    # [ ] TODO: higher order function (HOF). Have this function validate initial inputs and assert final output before sending
        # [ ] TODO: if numbers is None, do not bother recursing and return a new ListNode
        # [ ] TODO: 
    # Basecases
    # - use a helper function to recurse from facade
    # - if there are no numbers, return our output
    # 2. if the 


def main():
    nums1 = [1, 3, 10]
    nums2 = [-1, 3, 8]
    L1 = new_nodes(nums1)
    L2 = 


if __name__ == "__main__":
    main()

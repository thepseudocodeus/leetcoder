from typing import Optional, Dict, Any
from copy import deepcopy
from functools import singledispatch


class ListNode:
    def __init__(self, val: Optional[int] = 0, node: Optional["ListNode"] = None):
        self.val = val
        self.next = node


def to_list(head: ListNode):
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output


def to_dict(head: ListNode) -> Dict[Any, Any]:
    return {k: v for k, v in enumerate(to_list(head))}


@singledispatch
def show(param: Any, message: str = "") -> None:
    _ = message
    raise TypeError(f"{type(param)} is not handled.")


@show.register
def _(param: ListNode, message: str = "") -> None:
    _ = message
    elements_dict = to_dict(param)
    for k, v in elements_dict.items():
        print(f"Node #{k}: {v}")
    print("")


@show.register
def _(param: str, message: str) -> None:
    print(f"{message}")
    print(f"{param}")
    print("")


@show.register
def _(param: int, message: str) -> None:
    print(f"{message}")
    print(f"{param}")
    print("")


@show.register
def _(param: None, message: str = "") -> None:
    print(f"This message is empty: {message}")
    print(f"parameter value is: {param}")


@show.register
def _(param: list, message: str) -> None:
    print(f"{message}")
    for n in param:
        print(f"{n}")
    print("")


def length(head: Optional[ListNode]) -> int:
    count = 0
    tmp = deepcopy(head)
    while tmp:
        count += 1
        tmp = tmp.next
    return count


def merge(
    list1: Optional[ListNode] = None, list2: Optional[ListNode] = None
) -> ListNode:
    if not list1 and not list2:
        return None

    if not list1:
        return list2

    if not list2:
        return list1

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        # result1 = length(list1)
        # result2 = length(list2)
        # print(f"list1 has {result1} elements")
        # print(f"Current list1 value: {list1.val}")
        # print("----------------")
        # print(f"list2 has {result2} elements")
        # print(f"Current list2 value: {list2.val}")
        # print("----------------")
        # result3 = length(tail)

        # result4 = length(dummy)
        # print(f"tail has {result3} elements")
        # print(f"dummy has {result4} elements")
        # print("----------------")
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    tail.next = list1 or list2
    return dummy.next


def new_node(v: int) -> ListNode:
    if not v:
        return ListNode()

    return ListNode(v)


def new_nodes(vals: int) -> Optional[ListNode]:
    if not vals:
        return None

    dummy = ListNode()
    tail = dummy
    for n in vals:
        tail.next = new_node(n)
        tail = tail.next
    return dummy.next


def display(head: ListNode) -> None:
    values = to_list(head)
    for i, v in enumerate(values):
        print(f"Value #:{i + 1} = {v}")
    print("------------")


def main():
    tmp1 = []
    tmp2 = [-2, 3, 4, 7, 9]
    l1 = new_nodes(tmp1)
    l2 = new_nodes(tmp2)

    l3 = merge(l1, l2)
    show(l1, "Linked List #1")
    show(l2, "Linked List #2")
    show(l3, "Finished Linked List")


if __name__ == "__main__":
    main()

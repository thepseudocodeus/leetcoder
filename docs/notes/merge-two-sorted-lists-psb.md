---
id: hvjxgmv3175y3giwg7ks0kf
title: Psb_template
desc: ''
updated: 1759093667161
created: 1759092245796
---

📘 LeetCode Problem Definition (Math-English Invariant Structure)
1. Problem Name

Merge Two Sorted Lists

Given two lists containing integers in nondescending order, return the head of a linked list that merges the values from these list in nondescending order


1. Inputs (Given)
- list1: sequence of nodes with integer values and link to next node
- list2: ibid.
- Return a linked list from these that maintains the same nondescending order in a single list now

Type: sequence of nodes as linked lists with val and next fields

Constraints:

- 0 - 50 nodes
- -100 to 100 integer values
- value can be empty, none, etc
- node can be empty, none, etc
- can have duplicate integers

👉 Example:

Input: Two sorted linked lists L1 and L2.

Each contains between 0–50 integers, values between -100 and 100.

1. Outputs (Required Result)

Type: <describe type>

Properties: <key properties of the result>

👉 Example:

Output: A linked list containing all elements from L1 and L2, sorted in non-decreasing order.

4. Preconditions (Assumptions / Guarantees about Input)

- L1 and L2 are sorted in non-decreasing order
- Node is of type Optional[ListNode]



<assumptions given by problem that do not need to be re-checked>

👉 Example:

Both L1 and L2 are already sorted.

Each node contains a valid integer.

1. Postconditions (What Must Hold True After)

<output invariants that must always be satisfied>

👉 Example:

- Length(result) = Length(L1) + Length(L2).

- Every element in L1 and L2 appears exactly once in result.

- Result is sorted in non-decreasing order.

6. Process / Transformation (Declarative Steps)

<state how input is transformed into output, step by step>

👉 Example:

- If either list is empty, return the other.

- Otherwise, compare first elements of L1 and L2.

- Pick smaller element, attach to result, and recurse/iterate on remainder.

7. Edge Cases

<minimal, maximal, or special cases to confirm correctness>

👉 Example:

- Both lists empty → return empty list.

- One list empty → return the other.

- Lists with duplicates → duplicates preserved.

✅ With this template, you’ll always:

Separate assumptions from guarantees.

Clearly define invariants before coding.
---
id: hvjxgmv3175y3giwg7ks0kf
title: Psb_template
desc: ''
updated: 1759092252851
created: 1759092245796
---

📘 LeetCode Problem Definition (Math-English Invariant Structure)
1. Problem Name

<Title of the LeetCode problem>

2. Inputs (Given)

Type: <describe types of inputs>

Constraints: <size limits, value ranges, etc.>

👉 Example:

Input: Two sorted linked lists L1 and L2.

Each contains between 0–50 integers, values between -100 and 100.

3. Outputs (Required Result)

Type: <describe type>

Properties: <key properties of the result>

👉 Example:

Output: A linked list containing all elements from L1 and L2, sorted in non-decreasing order.

4. Preconditions (Assumptions / Guarantees about Input)

<assumptions given by problem that do not need to be re-checked>

👉 Example:

Both L1 and L2 are already sorted.

Each node contains a valid integer.

5. Postconditions (What Must Hold True After)

<output invariants that must always be satisfied>

👉 Example:

Length(result) = Length(L1) + Length(L2).

Every element in L1 and L2 appears exactly once in result.

Result is sorted in non-decreasing order.

6. Process / Transformation (Declarative Steps)

<state how input is transformed into output, step by step>

👉 Example:

If either list is empty, return the other.

Otherwise, compare first elements of L1 and L2.

Pick smaller element, attach to result, and recurse/iterate on remainder.

7. Edge Cases

<minimal, maximal, or special cases to confirm correctness>

👉 Example:

Both lists empty → return empty list.

One list empty → return the other.

Lists with duplicates → duplicates preserved.

✅ With this template, you’ll always:

Separate assumptions from guarantees.

Clearly define invariants before coding.
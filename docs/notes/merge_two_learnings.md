---
id: bsayx7di6zxpn3xqrrsghot
title: Merge_two_learnings
desc: ''
updated: 1759093036743
created: 1759083853614
---

#leetcode #linked-list #problem #psb #mathematical-thinking #learn #teach #record


🚀 Step 1: Redefine the Problem Mathematically

The original LeetCode problem is:

Merge two sorted linked lists into a single sorted list. Return the merged list.

Formal mathematical spec:

Input: two sequences 
𝐿
1
,
𝐿
2
∈
𝑍
∗
L
1
	​

,L
2
	​

∈Z
∗
 (finite lists of integers).

Preconditions: 
𝐿
1
,
𝐿
2
L
1
	​

,L
2
	​

 are non-decreasing.

Output: 
𝐿
3
∈
𝑍
∗
L
3
	​

∈Z
∗
.

Postconditions:

Sortedness invariant: 
𝐿
3
L
3
	​

 is non-decreasing.

Length invariant: 
∣
𝐿
3
∣
=
∣
𝐿
1
∣
+
∣
𝐿
2
∣
∣L
3
	​

∣=∣L
1
	​

∣+∣L
2
	​

∣.

Multiset invariant: The elements of 
𝐿
3
L
3
	​

 equal the multiset union of 
𝐿
1
L
1
	​

 and 
𝐿
2
L
2
	​

.

This is our truth. Every implementation must prove these invariants.

🚀 Step 2: Prototype in Haskell (Recursive, Declarative)
Haskell implementation
-- src/Merge.hs
module Merge where

data List a = Nil | Cons a (List a) deriving (Eq, Show)

-- Merge two sorted lists
merge :: Ord a => List a -> List a -> List a
merge Nil ys = ys
merge xs Nil = xs
merge (Cons x xs) (Cons y ys)
  | x <= y    = Cons x (merge xs (Cons y ys))
  | otherwise = Cons y (merge (Cons x xs) ys)

-- Helpers
fromList :: [a] -> List a
fromList []     = Nil
fromList (x:xs) = Cons x (fromList xs)

toList :: List a -> [a]
toList Nil         = []
toList (Cons x xs) = x : toList xs


Notice: recursion naturally expresses "take the smaller head, recur on the rest," mirroring the math.

🚀 Step 3: Validate with QuickCheck (Invariant Testing)
-- test/MergeSpec.hs
module MergeSpec where

import Test.QuickCheck
import Data.List (sort)
import Merge

prop_mergePreservesMultiset :: [Int] -> [Int] -> Bool
prop_mergePreservesMultiset xs ys =
  let l1 = fromList (sort xs)
      l2 = fromList (sort ys)
      merged = toList (merge l1 l2)
  in merged == sort (xs ++ ys)

return []  -- Template Haskell trick for quickCheckAll

runTests :: IO Bool
runTests = $quickCheckAll

Run it:
stack test


QuickCheck will automatically generate hundreds of random test cases, including weird corner cases (empty lists, duplicates, negative numbers, etc.), and verify the invariants.

At this point, we have mathematical confidence that our recursive spec matches the problem definition.

🚀 Step 4: Translate Key Invariants to Python Tests

Using Hypothesis in Python:

from hypothesis import given, strategies as st

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for x in lst:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def linked_to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

@given(
    a=st.lists(st.integers(-100, 100), max_size=50),
    b=st.lists(st.integers(-100, 100), max_size=50),
)
def test_merge_invariants(a, b):
    a, b = sorted(a), sorted(b)
    l1, l2 = build_linked_list(a), build_linked_list(b)
    out = linked_to_list(merge_iter(l1, l2))
    assert out == sorted(a + b)


Now Python is constrained by the same invariants Haskell confirmed.

🚀 Step 5: Python Iterative Implementation (Optimized)

Here’s the Pythonic solution (recommended style: while loop + dummy node):

def merge_iter(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


✅ Optimization reason: avoids recursion depth limits, uses O(1) extra space, works with Python’s pointer semantics naturally.

🚀 Step 6: Crash Course in Haskell Setup in Devcontainer
devcontainer.json
{
  "name": "Python + Haskell",
  "image": "mcr.microsoft.com/vscode/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/devcontainers/features/haskell:1": {},
    "ghcr.io/devcontainers/features/python:1": {}
  },
  "postCreateCommand": "stack setup && stack build"
}

Dockerfile (optional, if you want control)
FROM haskell:9.2
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install hypothesis pytest

VS Code Extensions

haskell.haskell (Haskell LSP support).

ms-python.python.

ms-toolsai.jupyter (if you like notebooks).

Project structure
/project
  /src
    Merge.hs
  /test
    MergeSpec.hs
  py/
    merge.py
    test_merge.py
  devcontainer.json
  stack.yaml
  package.yaml

🚀 Step 7: Learning Cycle (Markdown Crash Course for Haskell)
docs/01-intro.md

Haskell is about expressing mathematics as code.

Always start with type signatures (like equations).

Build small functions, test them in ghci.

Example: implement sum, reverse, etc.

Run stack ghci → experiment interactively.

docs/02-invariants.md

Always state invariants before writing code.

Example: “merge must preserve length and sortedness.”

Express these as properties in QuickCheck.

Properties → automated reasoning → confidence.

docs/03-composing.md

Solve tiny subproblems first.

Use fromList / toList helpers to bridge testing.

Compose into pipelines.

When stuck: test tiny pieces, not whole problem.

docs/04-side-effects.md

Haskell discourages side effects → you’re forced to reason clearly.

Use pure recursion, HOFs (map, foldr, etc.).

This matches the “math → code” process exactly.

docs/05-translation.md

After you’re certain in Haskell, translate to Python.

Python adds performance-friendly tools (loops, dummy nodes).

But invariants are unchanged.

Hypothesis = your QuickCheck for Python.
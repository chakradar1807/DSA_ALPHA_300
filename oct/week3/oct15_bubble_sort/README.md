## Variant 1: Sort Array By Parity II (LeetCode 922)
**Approach:** Uses two pointers (`even` starting at index 0 and `odd` starting at index 1). It scans using separate while loops to find misplaced elements—an even number at an odd index or vice versa—and swaps them in-place until both pointers traverse the array.
**Time:** O(n)
**Space:** O(1)
**Edge case missed first time:** Arrays with the minimum length of 2 where elements are already in correct parity positions.

## Variant 2: Height Checker (LeetCode 1051)
**Approach:** Copy the heights, sort the copy with my own bubble sort, then count the positions where the original and the sorted copy differ.
**Time:** O(n^2)
**Space:** O(n)
**Edge case missed first time:** Heights arrays that are already completely sorted, ensuring the early-exit flag correctly bypasses unnecessary passes.

## Variant 3: Sort Colors (LeetCode 75)
**Approach:** Dutch national flag with low, mid and high pointers. A 0 swaps with low and both advance. A 1 advances mid. A 2 swaps with high and only high moves, because the swapped-in value is unchecked.
**Time:** O(n)
**Space:** O(1)
**Edge case missed first time:** Arrays containing only one unique color or already grouped adjacent numbers like `[0, 0, 1, 2, 2]`.

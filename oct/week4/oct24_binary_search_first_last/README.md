# Day 24: Binary Search Boundaries & Range Applications

## 1. Find First and Last Position of Element in Sorted Array (LeetCode 34)
- **Approach:** Implemented a binary search bound helper to find the lower bound index of the target and the lower bound of `target + 1` minus one, accurately capturing the exact starting and ending range boundaries.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** When the target value does not exist in the array, correctly returning `[-1, -1]`.

## 2. Count Occurrences in Sorted Array (GFG)
- **Approach:** Located the first and last occurrences of the target using two independent binary search routines, calculating total frequency via `last - first + 1`.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Handling targets completely missing from the array (returning `0`).

## 3. Floor and Ceil in a Sorted Array (GFG Combined)
- **Approach:** Used specialized binary search passes to determine both the floor (largest element $\le x$) and the ceil (smallest element $\ge x$) efficiently within logarithmic time.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Query values smaller than the minimum element or larger than the maximum element in the array.

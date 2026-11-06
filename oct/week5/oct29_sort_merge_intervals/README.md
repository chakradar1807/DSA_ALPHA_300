# Day 29: Sorting & Merge Intervals

## 1. Merge Intervals (LeetCode 56)
- **Approach:** Sorted intervals by their starting boundaries and performed an in-place linear scan using a pointer `k` to merge overlapping intervals.
- **Complexity:** $O(n \log n)$ time and $O(1)$ extra space (excluding sorting stack space).
- **Edge Case Missed:** Unsorted input arrays or intervals touching at a single endpoint (e.g., `[1, 4]` and `[4, 5]`).

## 2. Insert Interval (LeetCode 57)
- **Approach:** Located the insertion and overlap indices efficiently using binary search boundaries, merging overlapping ranges before reconstructing the final list slices.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Missed:** The new interval falling completely before all existing intervals, completely after them, or covering all existing intervals.

## 3. Non-overlapping Intervals (LeetCode 435)
- **Approach:** Sorted intervals by their **end times** rather than start times. Greedily kept intervals that start at or after the previous end time to maximize non-overlapping selections, then subtracted from the total count.
- **Complexity:** $O(n \log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Input arrays with zero overlaps or cases where all intervals are identical.

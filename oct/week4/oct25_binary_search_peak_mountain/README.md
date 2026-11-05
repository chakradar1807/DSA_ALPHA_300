# Day 25: Binary Search Peak & Mountain Array Variants

## 1. Find Peak Element (LeetCode 162)
- **Approach:** Applied binary search by comparing `nums[mid]` with `nums[mid + 1]`. If the slope is rising, a peak is guaranteed on the right; if falling, a peak exists on the left.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Peaks located at the very boundaries (index `0` or index `n-1`).

## 2. Peak Index in a Mountain Array (LeetCode 852)
- **Approach:** Utilized the same slope-comparison binary search logic as LeetCode 162, taking advantage of the strict mountain shape guarantee to converge directly onto the peak index.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Arrays with minimum length constraints (e.g., length of 3).

## 3. Find in Mountain Array (LeetCode 1095)
- **Approach:** Conducted three binary searches: first to find the peak index, second to search the strictly increasing left side, and third to search the strictly decreasing right side with reversed comparison rules.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** When the target is present on both the rising and falling slopes (ensuring the left-most occurrence is returned).

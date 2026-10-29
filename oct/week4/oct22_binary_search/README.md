# Day 22: Binary Search

## 1. Binary Search (LeetCode 704)
- **Approach:** Standard iterative binary search. Maintain two pointers (`low` and `high`), calculate the middle index, and adjust search boundaries based on whether the target is smaller or larger than the middle element.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Target smaller than the first element or larger than the last element resulting in a $-1$ return value.

## 2. Search Insert Position (LeetCode 35)
- **Approach:** Use binary search to find the target's exact index or determine the exact insertion position by tracking the convergent boundary pointers when the loop terminates.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Inserting a target that should be placed at index `0` or right at the end of the array (index `n`).

## 3. First Bad Version (LeetCode 278)
- **Approach:** Apply binary search across version ranges. When `isBadVersion(mid)` is true, record the candidate answer and search the left half (`right = mid - 1`) to find the *first* occurrence.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** When `n = 1` and version `1` is immediately bad.

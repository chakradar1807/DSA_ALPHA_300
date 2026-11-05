# Day 26: Binary Search on Rotated Sorted Array

## 1. Search in Rotated Sorted Array (LeetCode 33)
- **Approach:** Apply modified binary search by checking which half of the array (`left` or `right`) is strictly sorted at each midpoint. Determine if the target lies within the boundaries of the sorted half to narrow the search space logarithmically.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Arrays with only 1 or 2 elements, or targets located at the exact pivot or boundary indices.

## 2. Find Minimum in Rotated Sorted Array (LeetCode 153)
- **Approach:** Use binary search to locate the pivot (minimum element) by comparing `nums[mid]` with `nums[high]`. If `nums[mid] > nums[high]`, the minimum lies on the right half; otherwise, it is at `mid` or on the left half.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** Unrotated arrays where the minimum element is at index `0`.

## 3. Find Rotation Count in Sorted Array (GFG)
- **Approach:** Re-utilize the minimum element binary search logic from LeetCode 153. The total rotation count of a sorted array is precisely equal to the index of its minimum element.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** An array that was rotated $0$ times (returning `0` instead of throwing an out-of-bounds error).

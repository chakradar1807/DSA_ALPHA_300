# Day 30: Sorting & Binary Search Combo

## 1. Longest Consecutive Sequence (LeetCode 128)
- **Approach:** Sorted the array in-place and performed a linear scan, tracking consecutive runs and safely skipping duplicate numbers.
- **Complexity:** $O(n \log n)$ time and $O(1)$ space (or $O(n)$ time and space using a hash set).
- **Edge Case Missed:** Empty arrays, arrays with all duplicate elements, and negative numbers.

## 2. 3Sum (LeetCode 15)
- **Approach:** Sorted the array and used a fixed outer element paired with a shrinking two-pointer scan. Included explicit duplicate-skipping logic for both the base number and inner pointers.
- **Complexity:** $O(n^2)$ time and $O(1)$ auxiliary space.
- **Edge Case Missed:** Arrays containing all zeros (`[0, 0, 0, 0]`) or fewer than 3 elements.

## 3. Two Sum II - Input Array Is Sorted (LeetCode 167)
- **Approach:** Leveraged the sorted property of the input array using two pointers starting at opposite ends, moving inward based on sum comparisons to return 1-based indices.
- **Complexity:** $O(n)$ time and $O(1)$ space.
- **Edge Case Missed:** Pairs located at the very extremes or arrays with duplicate elements.

# Day 12: String Compression, Consecutive Runs & Duplicate Removal

## 1. String Compression (LeetCode 443)
- **Approach:** Used a read pointer to scan runs of identical characters and an `ans` (write) pointer to update the character array in-place, appending multi-digit counts character by character.
- **Complexity:** $O(n)$ time and $O(1)$ extra space.
- **Edge Case Handled:** Single-character runs, runs with counts $\ge 10$, and all unique characters.

## 2. Consecutive Characters (LeetCode 1446)
- **Approach:** Traversed the string using two pointers (`i` and `j`) to locate blocks of matching consecutive characters and tracked the maximum power length.
- **Complexity:** $O(n)$ time and $O(1)$ space.
- **Edge Case Handled:** Single-character strings and strings with no repeating characters.

## 3. Remove All Adjacent Duplicates in String II (LeetCode 1209)
- **Approach:** Repeatedly scanned the string using a flag loop to find and slice out contiguous character segments of length `k`.
- **Complexity:** $O(n^2)$ time in the worst case due to string slicing, and $O(n)$ space.
- **Edge Case Handled:** Cascading cancellations and `k` values equal to string length.

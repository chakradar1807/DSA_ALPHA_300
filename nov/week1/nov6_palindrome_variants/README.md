# Day 6: Palindrome Construction & Frequency Bounds

## 1. Construct K Palindrome Strings (LeetCode 1400)
- **Approach:** Counted character frequencies using a hash map and counted elements with odd frequencies, verifying that the odd count is at most `k` and `k` does not exceed the total string length (`odd_count <= k <= len(s)`).
- **Complexity:** $O(n)$ time and $O(1)$ space (since character set is bounded).
- **Edge Case Missed:** `k > len(s)` (returning false) or `k < odd_count` (returning false).

## 2. Longest Palindrome (LeetCode 409)
- **Approach:** Maintained a running count of odd-frequency characters using a dictionary hash map during iteration to determine the longest possible palindrome length.
- **Complexity:** $O(n)$ time and $O(1)$ space.
- **Edge Case Missed:** Strings with all unique characters or all even-frequency characters.

## 3. Valid Palindrome II (LeetCode 680)
- **Approach:** Evaluated string symmetry with two pointers moving inward, allowing at most one character deletion upon encountering a mismatch.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space.
- **Edge Case Missed:** Strings already palindromic or strings requiring deletion at the very extremes.

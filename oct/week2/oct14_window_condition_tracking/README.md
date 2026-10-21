# Day 14 - Window + Condition Tracking

## 1. Max Consecutive Ones III (LeetCode 1004)
* **Approach:** Variable-size sliding window tracking zero counts. Expands the `right` pointer and increments `zeroCount` when a zero is encountered. If `zeroCount` exceeds `k`, shrinks from the `left` until constraints are met, updating the maximum window length.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case handled:** $k = 0$ (no flips allowed) and arrays containing all zeros or all ones.

---

## 2. Longest Repeating Character Replacement (LeetCode 424)
* **Approach:** Uses a sliding window with character frequency tracking. Maintains `max_freq` of any single character in the current window. If remaining characters (`window_size - max_freq`) exceed `k`, shrinks from the left.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$ (bounded by alphabet size of 26).
* **Edge case handled:** Strings with all identical characters or where $k$ is large enough to replace the entire string.

---

## 3. Longest Substring Without Repeating Characters (LeetCode 3)
* **Approach:** Utilizes a hash map to store the last seen index of each character. When a duplicate character is found inside the current window, the `left` pointer jumps directly past its previous occurrence in $O(1)$ time.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(min(n, \Sigma))$
* **Edge case handled:** Empty strings, strings with all unique characters, and strings with repeating identical characters like `"bbbbb"`.

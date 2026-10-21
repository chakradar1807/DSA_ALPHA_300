# Day 12 - Variable-Size Sliding Window & Prefix Sums

## Variant: Maximum Number of Vowels in a Substring of Given Length (LeetCode 1456)
* **Approach:** Fixed-size window included as a warm-up before variable-size problems. Counts vowels in the first window of size $k$, then slides right one step at a time, updating counts in $O(1)$ time and returning early if the maximum possible count $k$ is reached.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case handled:** Strings with no vowels or strings where every character is a vowel.

---

## 1. Minimum Size Subarray Sum (LeetCode 209)
* **Approach:** Uses a variable-size sliding window with `left` and `right` pointers. Expands the `right` pointer to add elements to a running sum. When the sum reaches or exceeds the target, records the window length and shrinks from the left to find the minimum possible length.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case handled:** No subarray reaches the target (returns `0`) and single-element windows that immediately meet the target.

---

## 2. Subarray Sum Equals K / Longest Subarray with Sum K (LeetCode 560 / GFG)
* **Approach:** Utilizes a prefix sum running accumulator combined with a hash map frequency dictionary (`d = {0: 1}`) to track and count matching subarrays in a single linear pass.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(n)$
* **Edge case handled:** Subarrays starting precisely from index 0 and multiple overlapping valid subarrays.

---

## 3. Fruit Into Baskets (LeetCode 904)
* **Approach:** Variable-size sliding window with a frequency hash map (`defaultdict`). Expands `window_end` to collect fruits, and whenever distinct fruit types exceed 2, shrinks `window_start` from the left, deleting map keys when their counts drop to zero.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$ (hash map holds at most 3 fruit types at any time).
* **Edge case handled:** Arrays containing only one unique fruit type or exactly two unique fruit types.

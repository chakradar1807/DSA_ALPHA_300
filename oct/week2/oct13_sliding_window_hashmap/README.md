# Day 13 - Sliding Window with Hash Map & Frequency Tracking

## 1. Contains Duplicate II (LeetCode 219)
* **Approach:** Uses a variable-size sliding window hash set of maximum size $k$. As the window advances, it checks for existence in $O(1)$ time and removes elements falling out of the window boundary from the left.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(k)$
* **Edge case handled:** Arrays with no duplicates or duplicate indices spaced further apart than $k$.

---

## 2. Find All Anagrams in a String (LeetCode 438)
* **Approach:** Maintains a sliding character frequency counter of size equal to pattern `p`. To comply with strict constraints avoiding `.append()`, it uses a two-pass approach: first counting total matches to pre-allocate the exact result array, then populating it via direct index assignment.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$ (hash map constrained by fixed alphabet size).
* **Edge case handled:** Strings where `s` is shorter than `p` (returns empty array immediately).

---

## 3. Permutation in String (LeetCode 567)
* **Approach:** Uses a fixed-size sliding window counter matching the length of `s1`. Slides across `s2` by incrementing the incoming character count and decrementing/dropping the outgoing character count at each step while comparing dictionaries.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$ (frequency maps bounded by character set size).
* **Edge case handled:** When `s1` is longer than `s2` or exact match occurs at the very final indices.

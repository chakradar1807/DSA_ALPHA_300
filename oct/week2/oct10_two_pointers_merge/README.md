# Day 10 - Two Pointers for Merging & Partitioning

## 1. Merge Sorted Array (LeetCode 88)
* **Approach:** Merges two sorted arrays in-place by starting from the back. Uses three pointers: `i` at the end of `nums1`'s valid elements, `j` at the end of `nums2`, and `k` at the very end of `nums1`. Compares elements and places the larger one at index `k`, working backwards to prevent overwriting.
* **Time Complexity:** $O(m + n)$
* **Space Complexity:** $O(1)$ (in-place modification)
* **Edge case missed first time:** When `nums2` is empty (`n = 0`), when `nums1` has no real values (`m = 0`), or when all elements in `nums2` are smaller than everything in `nums1`.

---

## 2. Squares of a Sorted Array (LeetCode 977)
* **Approach:** Takes advantage of the fact that the largest squares in a sorted array (containing negatives) will always lie at the outer edges. Uses two pointers at both ends (`left` and `right`), compares their absolute values, and populates a pre-allocated result array from the back to the front.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(n)$ (for the new result array)
* **Edge case missed first time:** Arrays consisting entirely of negative numbers, entirely of positive numbers, or a single-element array.

---

## 3. Sort Array By Parity (LeetCode 905)
* **Approach:** Uses a read pointer (`i`) to scan through the array and a write pointer (`j`) to track where the next even number should be placed. When an even number is encountered, it swaps it with the element at index `j` and increments `j`.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** Arrays with all even numbers, all odd numbers, or a single-element array.

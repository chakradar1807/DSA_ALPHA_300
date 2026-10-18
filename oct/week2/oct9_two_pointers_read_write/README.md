# Day 9 - Two Pointers in the Same Direction (Read and Write)

## 1. Move Zeroes (LeetCode 283)
* **Approach:** Uses a read pointer (`right`) to scan the array and a write pointer (`left`) to track where the next non-zero element should go. Swaps non-zero elements to the front while maintaining their relative order.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$ (in-place modification)
* **Edge case missed first time:** Arrays with no zeros or all zeros.

---

## 2. Remove Duplicates from Sorted Array (LeetCode 26)
* **Approach:** Utilizes two pointers (`i` as the slow write pointer for unique elements, `j` as the fast read pointer). When a new unique element is found at `j`, `i` advances and updates `nums[i]`.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** An array with all duplicate elements or a single-element array.

---

## 3. Remove Element (LeetCode 27)
* **Approach:** Uses a read pointer to iterate through the array and a write pointer to overwrite elements that do not match the target value `val`, performing an in-place filtration.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** When `val` is not present in the array or when every element matches `val`.

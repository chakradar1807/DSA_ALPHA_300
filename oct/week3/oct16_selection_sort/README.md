# Day 16 - Sorting & Tracking Problems

## 1. Sort an Array (LeetCode 912)
* **Approach:** Implements an efficient sorting algorithm to sort an array of integers in ascending order without relying on built-in shorthand methods. Recursively divides the array and merges sorted halves.
* **Time Complexity:** $O(n \log n)$
* **Space Complexity:** $O(n)$
* **Edge case handled:** Arrays with negative numbers, duplicate values, and already sorted inputs.

---

## 2. Relative Ranks (LeetCode 506)
* **Approach:** Computes the relative ranks of athletes based on their scores. Maps scores to their original indices, sorts them in descending order, and assigns medals to the top three positions.
* **Time Complexity:** $O(n \log n)$
* **Space Complexity:** $O(n)$
* **Edge case handled:** Small arrays (fewer than 3 elements) and duplicate scores.

---

## 3. Third Maximum Number (LeetCode 414)
* **Approach:** Traverses the array while maintaining tracking variables for the maximum, second maximum, and third maximum distinct values, bypassing duplicates to guarantee uniqueness in a single pass.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case handled:** Arrays with fewer than 3 distinct elements and negative integers.

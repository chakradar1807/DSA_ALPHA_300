# Day 7 - Array Rotation & Reversals

## 1. Rotate Array (LeetCode 189)
* **Approach:** Rotates the array to the right by $k$ steps in-place using the three-reverse algorithm. First, reverse the entire array, then reverse the first $k$ elements, and finally reverse the remaining elements.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** When $k$ is greater than the length of the array (`k > n`), handled using `k = k % n`.

---

## 2. Rotate String (LeetCode 796) / Rotate Left
* **Approach:** Validates if string `s` can become `goal` through rotation. Uses the concatenation trick `goal in (s + s)`, which contains all possible rotations as substrings.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(n)$
* **Edge case missed first time:** Strings of unequal lengths returning `False` immediately.

---

## 3. Reverse String II / Reverse Array in Groups (LeetCode 541 / GFG Equivalent)
* **Approach:** Iterates through the array/string in steps of $2k$ (or group size $k$), utilizing a reusable two-pointer reverse helper function to reverse specific segments while safely handling trailing elements shorter than $k$.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(n)$ (due to string-to-list conversion)
* **Edge case missed first time:** Last group having fewer than $k$ elements, handled safely using `min()`.

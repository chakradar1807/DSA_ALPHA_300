# Day 6 - Prefix Sums

## 1. Running Sum of 1d Array (LeetCode 1480)
* **Approach:** Build a separate prefix list in a single pass without mutating the original input array. Each element in the new list is calculated by adding the current input number to the previous running sum.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(n)$ (since a separate output list is created)
* **Edge case missed first time:** (Add your edge case here, e.g., a single-element array)

---

## 2. Find Pivot Index (LeetCode 724)
* **Approach:** Track the total sum of the array as `rightSum` and maintain a running `leftSum` starting at 0. Iterate through the array, reducing `rightSum` by the current element and checking if `leftSum == rightSum` before adding the current element to `leftSum`.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** (Add your edge case here, e.g., pivot at index 0 or no pivot found)

---

## 3. Range Sum Query - Immutable (LeetCode 303)
* **Approach:** Precompute and store a prefix sum array inside the class initializer (`__init__`). For each range query (`sumRange`), answer it in constant time by subtracting the prefix sum just before `left` from the prefix sum at `right`.
* **Time Complexity:** 
  * Initialization (`__init__`): $O(n)$
  * Query (`sumRange`): $O(1)$
* **Space Complexity:** $O(n)$ to store the prefix sum array.
* **Edge case missed first time:** (Add your edge case here, e.g., `left = 0` or when `left == right`)

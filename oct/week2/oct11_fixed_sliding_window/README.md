# Day 11 - Fixed-Size Sliding Window

## 1. Maximum Average Subarray I (LeetCode 643)
* **Approach:** Computes the sum of the first $k$ elements to initialize a window. Slides the window across the array in $O(1)$ per step by adding the incoming element and dropping the outgoing element, tracking the maximum sum manually using conditional checks (avoiding `max()`).
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** Arrays containing all negative numbers where initializing `max_sum = 0` would fail (handled by initializing with the first window's sum).

---

## 2. Max Sum Subarray of Size K (GFG)
* **Approach:** Applies the fixed-size sliding window technique to find the maximum subarray sum of length $k$. Maintains a running sum by sliding the window one position right at a time.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** When the array length is smaller than $k$.

---

## 3. Mean of Array After Removing Some Elements (LeetCode 1619)
* **Approach:** Removes the bottom 5% and top 5% of elements from the array to find the mean of the remaining 90%. Utilizes a heap-based approach (`heapq.nsmallest` and `heapq.nlargest`) to extract extremes efficiently in $O(n \log k)$ time without violating the no-sorting rule.
* **Time Complexity:** $O(n \log k)$ where $k$ is $5\%$ of $n$.
* **Space Complexity:** $O(k)$ for storing the extreme elements.
* **Edge case missed first time:** Large input values exceeding small fixed-bucket ranges and array lengths that do not divide cleanly by 20.

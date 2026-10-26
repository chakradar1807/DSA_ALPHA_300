# Day 20: Counting Sort & Frequency Variants

## 1. H-Index (LeetCode 274)
- **Approach:** Count paper frequencies using a bucket array capped at $n$ and compute cumulative sums backwards to find the maximum valid $h$-index in linear time without comparison sorting.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Missed:** When all papers have zero citations.

## 2. Valid Anagram (LeetCode 242)
- **Approach:** Maintain a fixed-size frequency array of size $26$ to track character increments from string `s` and decrements from string `t` in a single pass.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space.
- **Edge Case Missed:** Strings of differing lengths or empty string inputs.

## 3. Minimum Number of Moves to Seat Everyone (LeetCode 2037)
- **Approach:** Use frequency counting arrays to order seat and student positions into non-decreasing sequences without using `.sort()`, then sum absolute coordinate differences pairwise.
- **Complexity:** $O(n + k)$ time and $O(k)$ space, where $k$ is the maximum coordinate value.
- **Edge Case Missed:** When all students are already occupying their exact corresponding seats.

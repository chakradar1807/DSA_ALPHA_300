# Day 18: Frequency Sorting, Custom Ordering & String Reorganization

## 1. Custom Sort String (LeetCode 791)
- **Approach:** Counted frequencies of characters in `s`, appended them matching the specified custom `order`, and finished by appending any leftover characters.
- **Complexity:** $O(n + m)$ time where $n$ is the length of `s` and $m$ is the length of `order`, with $O(n)$ space.
- **Edge Case Handled:** Characters in `s` not found in `order`, and duplicate characters within `s`.

## 2. Reorganize String (LeetCode 767)
- **Approach:** Tracked character counts to ensure no single character exceeded $(n + 1) // 2$, then populated alternating positions to guarantee no adjacent matching characters.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space (bounded by the alphabet size).
- **Edge Case Handled:** Impossible reorganizations returning empty strings, single-character strings, and all-even character counts.

## 3. Sort Characters By Frequency (LeetCode 451)
- **Approach:** Counted all character frequencies, sorted the pairs by count in descending order, and rebuilt the final string by multiplying each character by its frequency.
- **Complexity:** $O(n + u \log u)$ time where $u$ is the number of distinct characters, and $O(n)$ space.
- **Edge Case Handled:** Unique single-character strings, uniformly distributed characters, and ties in frequency counts.

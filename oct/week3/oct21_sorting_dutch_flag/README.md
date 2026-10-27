# Sorting Variants and Advanced Applications

## 1. Rearrange Array Elements by Sign (LeetCode 2149)
- **Approach:** Maintain separate pointers for positive and even indices (`pos`) and negative and odd indices (`neg`), filling a pre-allocated result array in a single linear pass.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Missed:** Arrays with unequal counts of positive and negative numbers (though constraints guarantee equal distribution).

## 2. Maximum Product of Three Numbers (LeetCode 628)
- **Approach:** Track the three largest values and two smallest values in a single linear scan to find the maximum product of triplets without using built-in sorting functions.
- **Complexity:** $O(n)$ time and $O(1)$ extra space.
- **Edge Case Missed:** Arrays containing negative numbers where multiplying two large negative minimums yields a larger product than positive numbers.

## 3. Largest Number (LeetCode 179)
- **Approach:** Convert numbers to strings and sort them using a custom comparator based on concatenated string values (`a + b` vs `b + a`) via manual sorting, ensuring the optimal greedy arrangement.
- **Complexity:** $O(n^2)$ time due to custom sorting and $O(n)$ space.
- **Edge Case Missed:** Arrays consisting entirely of zeros (e.g., `[0, 0]` returning `"0"` instead of `"00"`).

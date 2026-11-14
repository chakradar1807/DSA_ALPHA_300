# Day 13: Bidirectional Mappings, Isomorphic Strings & Patterns

## 1. Find and Replace Pattern (LeetCode 890)
- **Approach:** Implemented dual forward and backward dictionaries (`forward` and `backward`) to ensure a strict one-to-one bijection between the characters of each candidate word and the target pattern, utilizing a list comprehension instead of `.append()`.
- **Complexity:** $O(N \cdot K)$ time where $N$ is the number of words and $K$ is the word length, with $O(1)$ auxiliary space for character alphabets.
- **Edge Case Handled:** Words with mismatched unique character mappings or length discrepancies.

## 2. Isomorphic Strings (LeetCode 205)
- **Approach:** Tracked the last seen character indices of both strings simultaneously on every iteration to verify that character appearance patterns align symmetrically between `s` and `t`.
- **Complexity:** $O(n)$ time and $O(1)$ space (bounded by character set size).
- **EdgeCase Handled:** Strings with repeating structures, mismatched lengths, or overlapping conflicting mappings.

## 3. Word Pattern (LeetCode 290)
- **Approach:** Split the sentence into words and checked string-to-pattern bijection using prefixed tuple keys (`("p", p)` and `("w", w)`) inside a unified hash map.
- **Complexity:** $O(n)$ time and $O(n)$ space for storing words and mappings.
- **Edge Case Handled:** Length mismatches between pattern tokens and sentence words, and many-to-one mapping violations.

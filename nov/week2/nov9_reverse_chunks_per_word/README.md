# Day 9: Reverse Chunks, Prefixes & Vowels

## 1. Reverse Prefix of Word (LeetCode 2000)
- **Approach:** Located the first occurrence of the target character `ch`, then manually constructed the resulting string by appending the reversed prefix and the remaining suffix in order.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Handled:** Characters not present in the word (returning the original string unchanged) or characters located at the very beginning/end.

## 2. Reverse Vowels of a String (LeetCode 345)
- **Approach:** Used inward-moving two pointers on a character list, checking for vowel occurrences (`a, e, i, o, u` case-insensitively) and swapping them in-place while leaving non-vowels untouched.
- **Complexity:** $O(n)$ time and $O(n)$ auxiliary space.
- **Edge Case Handled:** Strings with no vowels, all vowels, or single-character strings.

## 3. Reverse Words in A String III (LeetCode 557)
- **Approach:** Converted the string into a mutable character list and iterated through indices to locate spaces, reusing an in-place two-pointer reversal helper function (`reverse_chars`) to reverse each individual word without using `.split()` or forbidden slice assignments.
- **Complexity:** $O(n)$ time and $O(n)$ space (earned **0 ms runtime**).
- **Edge Case Handled:** Multiple consecutive spaces or single-word strings.

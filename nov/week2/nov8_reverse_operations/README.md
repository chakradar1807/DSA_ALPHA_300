# Day 8: Advanced Reverse Operations & Two-Pointers

## 1. Reverse Only Letters (LeetCode 917)
- **Approach:** Utilized inward-moving left and right pointers, skipping non-alphabetic characters and swapping letter characters in-place using a character list.
- **Complexity:** $O(n)$ time and $O(n)$ space for the character array.
- **Edge Case Handled:** Strings with no letters, strings consisting entirely of special characters, or single-character strings.

## 2. Reverse String II (LeetCode 541)
- **Approach:** Processed the string in chunks of `2k`, reversing only the first `k` characters of each chunk using an in-place pointer swap while leaving the remaining `k` characters unchanged.
- **Complexity:** $O(n)$ time and $O(n)$ auxiliary space.
- **Edge Case Handled:** Strings shorter than `k` or lengths between `k` and `2k`.

## 3. Reverse Words in a String (LeetCode 151)
- **Approach:** Manually parsed words to eliminate extra spaces, reversed the full character collection, and then reversed each individual word back to its correct orientation using a modular helper function.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Handled:** Leading, trailing, and multiple consecutive spaces between words.

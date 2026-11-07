# Day 2: Character Transformation and Replacement

## 1. Defanging an IP Address (LeetCode 1108)
- **Approach:** Iterated through the IP address string character by character, replacing every occurrence of `'.'` with `"[.]"` and building a new formatted string.
- **Complexity:** $O(n)$ time and $O(n)$ space (where $n$ is the length of the IP address).
- **Edge Case Missed:** Addresses with unusual lengths or inputs without periods.

## 2. To Lower Case (LeetCode 709)
- **Approach:** Converted characters manually using ASCII ranges (`65 <= ord(ch) <= 90` for uppercase letters) by adding `32` to shift them to lowercase without using `.lower()`.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Missed:** Strings containing numbers, punctuation marks, or already lowercase letters.

## 3. Capitalize the Title (LeetCode 2129)
- **Approach:** Parsed words by space delimiters, checking word lengths to capitalize the first letter and lowercase the rest for words longer than 2 characters, or entirely lowercase short words.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Missed:** Titles with consecutive spaces, single-letter words, or words of exactly length 2.

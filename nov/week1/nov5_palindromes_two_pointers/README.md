# Day 5: Palindromes & Two-Pointer Expansion

## 1. Palindromic Substrings (LeetCode 647)
- **Approach:** Counted palindromic substrings by treating every index (and space between indices) as a center, expanding outward as long as characters matched.
- **Complexity:** $O(n^2)$ time and $O(1)$ space.
- **Edge Case Missed:** Single-character strings or strings with all identical characters.

## 2. Palindrome Number (LeetCode 9)
- **Approach:** Handled negative numbers, then mathematically reversed the integer digits using modulo and integer division to compare against the original copy.
- **Complexity:** $O(\log_{10} n)$ time and $O(1)$ space.
- **Edge Case Missed:** Negative numbers and numbers ending in zero (other than 0 itself).

## 3. Valid Palindrome (LeetCode 125)
- **Approach:** Cleaned the input string to retain only alphanumeric characters, converted to lowercase, and verified symmetry using inward-moving two pointers.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Missed:** Strings with only punctuation, spaces, or empty strings.

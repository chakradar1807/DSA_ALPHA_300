# Day 10: String Parsing, Character Distances & Traversal

## 1. Goal Parser Interpretation (LeetCode 1678)
- **Approach:** Parsed the command string using a manual while-loop pointer, translating tokens `'G'`, `'()'`, and `'(al)'` into their corresponding decoded characters.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Handled:** Commands starting or ending with various token types or single-character commands.

## 2. Shortest Distance to a Character (LeetCode 821)
- **Approach:** Applied a two-pass technique (forward and backward traversal) to track distances from occurrences of character `c` and stored minimum distances in pre-allocated arrays.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Handled:** Characters appearing only once, at the very edges, or multiple times throughout the string.

## 3. Length of Last Word (LeetCode 58)
- **Approach:** Traversed the string backwards from the last index, skipping trailing whitespaces and accumulating the length of the final word.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space.
- **Edge Case Handled:** Single-word strings or strings with multiple trailing spaces.

# Day 1: Length, Concatenation, and Basic String Operations

## 1. Length of Last Word (LeetCode 58)
- **Approach:** Scanned the string backward from the end, skipped all trailing whitespace characters, and counted characters of the final word until hitting another space or the beginning of the string.
- **Complexity:** $O(n)$ time and $O(1)$ space.
- **Edge Case Missed:** Strings with extensive leading/trailing spaces or a single-word string without spaces.

## 2. Longest Common Prefix (LeetCode 14)
- **Approach:** Found the minimum string length and scanned character columns vertically from index 0 across all strings, terminating immediately upon a character mismatch.
- **Complexity:** $O(S)$ time (where $S$ is the sum of all characters across strings) and $O(1)$ extra space.
- **Edge Case Missed:** An array containing a single string or an empty string element.

## 3. Count and Say (LeetCode 38)
- **Approach:** Iteratively generated the sequence up to $n$ by using two pointers to scan consecutive runs of identical digits, counting their frequencies and building the next term string representation.
- **Complexity:** Proportional to the sum of all generated term lengths, with $O(\text{length of current term})$ space.
- **Edge Case Missed:** Base case $n = 1$ returning `"1"` directly without looping.

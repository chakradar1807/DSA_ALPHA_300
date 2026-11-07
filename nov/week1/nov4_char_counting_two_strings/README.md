# Day 4: String Frequency & Hash Validation

## 1. Jewels and Stones (LeetCode 771)
- **Approach:** Iterated through each unique jewel character and accumulated its total occurrence count within the stones string.
- **Complexity:** $O(n + m)$ time and $O(1)$ space.
- **Edge Case Missed:** Empty jewels or stones strings, or strings with no matching characters.

## 2. Find Common Characters (LeetCode 1002)
- **Approach:** Tracked character frequencies using fixed-size integer arrays (size 26) across words, manually maintaining minimum frequency bounds without using `min()` or `.append()`, and reconstructing the result via pre-allocated list index assignment.
- **Complexity:** $O(N \cdot M)$ time and $O(1)$ auxiliary space.
- **Edge Case Missed:** Arrays with single words or words sharing zero common characters.

## 3. Ransom Note (LeetCode 383)
- **Approach:** Built a frequency hash map of magazine characters and verified whether the ransom note could be constructed by decrementing available counts.
- **Complexity:** $O(m + n)$ time and $O(1)$ space (since character set is limited to lowercase English letters).
- **Edge Case Missed:** Ransom notes longer than the available magazine string length.

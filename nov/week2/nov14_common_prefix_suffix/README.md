# Day 14: KMP Prefix-Suffix Arrays & String Prefix Matching

## 1. Longest Prefix Suffix (GeeksforGeeks)
- **Approach:** Applied the KMP algorithm's prefix function (`lps` array generation) to compute the length of the longest proper prefix which is also a suffix in linear time[cite: 1].
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Handled:** Strings with no proper prefix matching a suffix, overlapping prefixes/suffixes, and single-character strings.

## 2. Counting Words With a Given Prefix (LeetCode 2185)
- **Approach:** Iterated through the list of words, checking string length constraints and validating slices against the target prefix.
- **Complexity:** $O(N \cdot M)$ time where $N$ is the number of words and $M$ is the prefix length, with $O(1)$ auxiliary space.
- **Edge Case Handled:** Words shorter than the prefix length or prefixes longer than the candidate words.

## 3. Check If String Is a Prefix of Array (LeetCode 1961)
- **Approach:** Sequentially concatenated words from the array and checked equality against the target string `s` at each step, exiting early upon a match.
- **Complexity:** $O(N)$ time and $O(N)$ space for string accumulation.
- **Edge Case Handled:** Arrays where concatenated words exceed string `s` in length or fail to match completely.

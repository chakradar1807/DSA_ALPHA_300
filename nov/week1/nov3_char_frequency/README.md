# Day 3: Frequency Counting & Hash Maps

## 1. First Unique Character in a String (LeetCode 387)
- **Approach:** Counted character frequencies using a dictionary hash map in a first pass, then performed a second linear scan to return the index of the first character with a count of 1.
- **Complexity:** $O(n)$ time and $O(1)$ space (since the alphabet size is bounded to 26 characters).
- **Edge Case Missed:** Strings with all repeating characters (returning `-1`) or strings of length 1.

## 2. Minimum Number of Steps to Make Two Strings Anagram (LeetCode 1347)
- **Approach:** Counted character frequencies of both strings using fixed-size integer frequency arrays of size 26, then calculated the total absolute difference divided by 2 to determine minimum steps.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space.
- **Edge Case Missed:** Strings that are already identical anagrams (resulting in 0 steps).

## 3. Group Anagrams (LeetCode 49)
- **Approach:** Sorted each string's characters to create a canonical dictionary key, grouping anagrams into buckets using list concatenation without `.append()`.
- **Complexity:** $O(n \cdot k \log k)$ time and $O(n \cdot k)$ space (where $n$ is the number of strings and $k$ is the maximum string length).
- **Edge Case Missed:** Arrays containing empty strings (`[""]`) or single-character strings.

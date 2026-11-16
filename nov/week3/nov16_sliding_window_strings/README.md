# Day 16: Sliding Window Algorithms & Substring Optimizations

## 1. Longest Substring Without Repeating Characters (LeetCode 3)
- **Approach:** Iterated through candidate start positions using an inner exploration loop to find the longest contiguous block containing unique characters without duplication.
- **Complexity:** $O(n^2)$ time in the worst-case configuration and $O(k)$ space where $k$ is the character set size.
- **Edge Case Handled:** Empty strings, strings with identical repeating characters, and spaces or symbols.

## 2. Longest Repeating Character Replacement (LeetCode 424)
- **Approach:** Maintained a sliding window with a frequency map and a running maximum character frequency (`max_freq`), shrinking the window from the left whenever the number of replaceable characters exceeded `k`.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space (bounded by the alphabet size).
- **Edge Case Handled:** $k = 0$ (no replacements allowed), strings with all uniform characters, and large replacement budgets.

## 3. Find All Anagrams in a String (LeetCode 438)
- **Approach:** Used a fixed-size sliding window of length equal to pattern `p`, comparing `Counter` frequency dictionaries and pre-allocating result indices efficiently.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space for standard alphabet character storage.
- **Edge Case Handled:** Haystack strings shorter than pattern `p`, strings with no anagram occurrences, and overlapping anagram windows.

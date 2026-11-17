# Day 17: Prefix Sums, Vowel Substrings & Dictionary-Based Tries

## 1. Sum of Prefix Scores of Strings (LeetCode 2416)
- **Approach:** Built a custom Trie using nested plain dictionaries to track frequency counts of words passing through each prefix node, then summed up prefix scores for every word.
- **Complexity:** $O(\text{total characters})$ time and space.
- **Edge Case Handled:** Single words, identical words, and words that act as prefixes for longer words.

## 2. Count Vowel Substrings of a String (LeetCode 2062)
- **Approach:** Scanned the string with an index-tracking dictionary, checking contiguous vowel blocks and accumulating valid sequences containing all five vowels.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space.
- **Edge Case Handled:** Strings shorter than 5 characters, vowel runs missing one vowel, and consonant splits.

## 3. Count Vowel Strings in Ranges (LeetCode 2559)
- **Approach:** Manually constructed a prefix sum array (one slot longer than the words list) without `itertools.accumulate()`, answering each range query in $O(1)$ time.
- **Complexity:** $O(n + q)$ time and $O(n)$ space.
- **Edge Case Handled:** Queries covering a single word, queries covering the entire array, and single-letter words starting and ending with vowels.

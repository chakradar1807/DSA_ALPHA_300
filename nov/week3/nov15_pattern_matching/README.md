# Day 15: Pattern Matching, Substring Search & Repetition

## 1. Repeated String Match (LeetCode 686)
- **Approach:** Repeatedly concatenated string `a` until its length was at least equal to string `b`, then checked for containment with up to two additional repetitions to account for alignment offsets.
- **Complexity:** $O(N \cdot M)$ time and $O(N + M)$ auxiliary space.
- **Edge Case Handled:** Strings where `b` requires extra boundary padding across repetitions or where `b` cannot be formed by `a`.

## 2. Repeated Substring Pattern (LeetCode 459)
- **Approach:** Iterated through candidate block lengths `i` up to $n / 2$ that evenly divide the string length `n`, validating if repeating the prefix substring reconstructs the original string.
- **Complexity:** $O(n \cdot d)$ time where $d$ is the number of divisors of $n$, and $O(1)$ auxiliary space.
- **Edge Case Handled:** Prime-length strings, single-character strings, and uniformly repeating characters.

## 3. Find the Index of the First Occurrence in a String (LeetCode 28)
- **Approach:** Scanned through the haystack using a sliding window approach, matching the needle character by character starting from each valid index position.
- **Complexity:** $O(n \cdot m)$ time in the worst case and $O(1)$ space.
- **Edge Case Handled:** Needles longer than the haystack, needles equal to the haystack, and matches occurring near the end of the string.

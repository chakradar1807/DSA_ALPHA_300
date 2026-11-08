# Day 7: String Parsing, Segments & Pangrams

## 1. Number of Segments in a String (LeetCode 434)
- **Approach:** Counted segments by tracking character transitions between whitespace and non-whitespace characters using a boolean flag.
- **Complexity:** $O(n)$ time and $O(1)$ space.
- **Edge Case Missed:** Strings with only whitespace, leading/trailing spaces, or consecutive spaces.

## 2. Check if the Sentence Is Pangram (LeetCode 1832)
- **Approach:** Validated length constraints ($len(sentence) >= 26$) and iterated through ASCII values from 97 to 122 to ensure every lowercase English letter appeared in the sentence.
- **Complexity:** $O(n)$ time and $O(1)$ space.
- **Edge Case Missed:** Sentences with missing alphabet characters or uppercase letters (if not pre-normalized).

## 3.# Check Consonants and Vowels (GeeksforGeeks)

- **Approach:** Counted vowels and consonants by iterating through the string character by character, utilizing a pre-defined vowel lookup set (`{'a', 'e', 'i', 'o', 'u'}`) for $O(1)$ containment checks. Compared counts to return `1`, `-1`, or `0` based on the problem conditions.
- **Complexity:** $O(n)$ time and $O(1)$ auxiliary space.
- **Edge Case Handled:** Strings with all vowels, all consonants, or an equal balance of both.

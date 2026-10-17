# Day 8 - Two Pointers from the Ends

## 1. Valid Palindrome (LeetCode 125)
* **Approach:** Uses a two-pointer approach from both ends, filtering out non-alphanumeric characters and comparing characters case-insensitively (`.lower()`).
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(n)$ (for storing the filtered temporary string)
* **Edge case missed first time:** Strings with only punctuation (should evaluate as true) and empty strings.

---

## 2. Reverse String (LeetCode 344)
* **Approach:** Modifies the character list in-place using two pointers starting at the opposite ends, swapping elements and moving inward until they meet.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(1)$
* **Edge case missed first time:** A one-element list or an even/odd length array handling.

---

## 3. Reverse Vowels of a String (LeetCode 345)
* **Approach:** Converts the string to a list and uses two pointers to scan inward. When both pointers land on a vowel (checked against a predefined vowel collection), they swap places; otherwise, the respective pointer steps forward or backward.
* **Time Complexity:** $O(n)$
* **Space Complexity:** $O(n)$ (due to string-to-list conversion)
* **Edge case missed first time:** Strings with no vowels, all vowels, or mixed uppercase and lowercase vowels.

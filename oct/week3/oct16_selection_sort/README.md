# Day 16 - Selection Sort & Custom Ordering

## 1. Selection Sort (GFG)
* **Approach:** Repeatedly iterates through the unsorted portion of the array to find the minimum element's index, then swaps it into its correct position at the beginning. The sorted region grows by one element per pass without using built-in sort functions.
* **Time Complexity:** $O(n^2)$ in all cases because the inner scan always runs in full length.
* **Space Complexity:** $O(1)$ auxiliary space (in-place sorting, performs at most $n - 1$ swaps).
* **Edge case handled:** Already sorted arrays, single-element arrays, and arrays with duplicate elements.

---

## 2. K Smallest Elements using Selection (GFG / Variant of LeetCode 215)
* **Approach:** Instead of sorting the entire array, it executes only $k$ passes of selection sort. In each pass, it finds the smallest remaining element and places it into its final sorted slot, guaranteeing that the first $k$ positions hold the $k$ smallest values.
* **Time Complexity:** $O(n \cdot k)$
* **Space Complexity:** $O(1)$ auxiliary space.
* **Edge case handled:** $k = 0$, $k = 1$, and $k$ equal to the total length of the array.

---

## 3. Sort Characters By Frequency (LeetCode 451)
* **Approach:** Manually counts character frequencies into a dictionary (avoiding `Counter`). Extracts the unique character-count pairs and sorts them descending using a custom selection sort implementation, then rebuilds the output string by repeating each character by its frequency count.
* **Time Complexity:** $O(n + u^2)$, where $n$ is the string length and $u$ is the number of unique characters.
* **Space Complexity:** $O(u)$ for storing the character frequency dictionary.
* **Edge case handled:** Characters with equal frequencies, case sensitivity (uppercase vs lowercase), and strings containing digits or symbols.


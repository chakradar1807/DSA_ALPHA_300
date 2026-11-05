# Day 27: Binary Search in 2D Matrices

## 1. Search a 2D Matrix (LeetCode 74)
- **Approach:** Treated the 2D matrix as a flattened 1D array using single-index arithmetic (`mid // n` and `mid % n`) to perform standard binary search in logarithmic time.
- **Complexity:** $O(\log(m \times n))$ time and $O(1)$ space.
- **Edge Case Missed:** Empty matrices or 1x1 matrix configurations.

## 2. Row with Maximum Ones (GFG)
- **Approach:** Leveraged the property that each row is sorted (0s followed by 1s) by starting from the top-right corner. If a `1` is encountered, record the row index and move left; if a `0` is encountered, move down to the next row.
- **Complexity:** $O(n + m)$ time and $O(1)$ space.
- **Edge Case Missed:** Rows containing entirely 0s or entirely 1s, and scenarios where no row contains any 1s (returning `-1`).

## 3. Find a Peak Element II (LeetCode 1901)
- **Approach:** Applied binary search across the columns of the 2D matrix. For each middle column, found the row with the maximum element and checked its left and right neighbors to determine which half of the columns to search next.
- **Complexity:** $O(n \log m)$ time and $O(1)$ space.
- **Edge Case Missed:** Peak elements located at the extreme boundary columns ($j = 0$ or $j = n-1$).

# Day 11: 2D Grid Shifts, Number Rotations & String Rotations

## 1. Shift 2D Grid (LeetCode 1260)
- **Approach:** Flattened the 2D grid conceptually into a 1D sequence using integer division and modulo arithmetic, applying triple-reversal pointer logic to shift elements in-place.
- **Complexity:** $O(m \cdot n)$ time and $O(1)$ auxiliary space.
- **Edge Case Handled:** `k = 0` or `k` values greater than total grid elements (`k % n`).

## 2. Rotate Digits of a Number by K (GeeksforGeeks)
- **Approach:** Converted the number to a string, evaluated positive (left) or negative (right) rotation offsets using index slicing and concatenation, and converted the result back to an integer.
- **Complexity:** $O(N)$ time and $O(N)$ space where $N$ is the number of digits.
- **Edge Case Handled:** Negative shift values (right rotations) and large rotation values exceeding digit counts.

## 3. Rotate String (LeetCode 796)
- **Approach:** Validated that string lengths match, then checked whether `goal` exists within the concatenated string `s + s`.
- **Complexity:** $O(n)$ time and $O(n)$ space.
- **Edge Case Handled:** Strings of unequal lengths or completely non-matching characters.

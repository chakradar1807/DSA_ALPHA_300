# Day 23: Binary Search Range & Mathematical Applications

## 1. Valid Perfect Square (LeetCode 367)
- **Approach:** Apply binary search within the range `[2, x // 2]` for numbers greater than $1$. Compute mid-point squares to check for exact equality, adjusting pointers accordingly.
- **Complexity:** $O(\log x)$ time and $O(1)$ space.
- **Edge Case Missed:** Input values `0` and `1` which require immediate early returns.

## 2. Guess Number Higher or Lower (LeetCode 374)
- **Approach:** Use standard binary search between `1` and `n`. Query the pre-defined `guess(mid)` API to determine whether to search the lower or upper half of the range.
- **Complexity:** $O(\log n)$ time and $O(1)$ space.
- **Edge Case Missed:** When `n = 1` and the target pick is immediately correct.

## 3. Sqrt(x) (LeetCode 69)
- **Approach:** Implement binary search between `0` and `x` to find the integer square root. Store the maximum valid value where `mid * mid <= x` in an answer variable before narrowing towards the upper bound.
- **Complexity:** $O(\log x)$ time and $O(1)$ space.
- **Edge Case Missed:** Input numbers `0` and `1` returning their exact square roots without overflow.

# Day 17: Insertion Sort

## 1. Largest Perimeter Triangle (LeetCode 976)
- **Approach:** Sort the array in descending order using manual insertion sort, then iterate through consecutive triplets. The first triplet that satisfies the triangle inequality condition ($b + c > a$) yields the maximum possible perimeter.
- **Complexity:** $O(n^2)$ time and $O(1)$ extra space.
- **Edge Case Missed:** Arrays with no possible valid triangle (returning $0$) or arrays containing duplicate lengths.

## 2. Insertion Sort List (LeetCode 147)
- **Approach:** Maintain a dummy head for a new sorted linked list. Iterate through the original list node by node, finding the correct insertion point in the sorted portion using a pointer, and splice the current node into place.
- **Complexity:** $O(n^2)$ time and $O(1)$ space.
- **Edge Case Missed:** An empty linked list or a list with only a single node.

## 3. Array Partition (LeetCode 561)
- **Approach:** Sort the array in ascending order using custom insertion sort, then sum every alternate element starting from index $0$ to maximize the sum of minimum pairs.
- **Complexity:** $O(n^2)$ time and $O(1)$ space.
- **Edge Case Missed:** Arrays with negative numbers or odd-length constraints.

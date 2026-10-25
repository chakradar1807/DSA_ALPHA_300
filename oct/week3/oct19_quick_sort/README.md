# Day 19: Quick Sort & Quickselect Variants

## 1. K Closest Points to Origin (LeetCode 973)
- **Approach:** Computed Euclidean distances and applied the Quickselect algorithm with an in-place Lomuto partition function to find the $k$-th smallest distance boundary without fully sorting all points.
- **Complexity:** $O(n)$ average time and $O(n)$ space for distance storage.
- **Edge Case Missed:** When $k$ equals the total number of points or when multiple points share identical distances from the origin.

## 2. Top K Frequent Elements (LeetCode 347)
- **Approach:** Counted frequencies manually into a dictionary, transferred items into an array, and sorted them using manual insertion sort by frequency in descending order without using `heapq`, `Counter`, or `.sort()`.
- **Complexity:** $O(n^2)$ time (due to manual insertion sort on unique elements) and $O(n)$ space.
- **Edge Case Missed:** When $k$ equals the number of unique elements in the frequency dictionary.

## 3. Wiggle Sort II (LeetCode 324)
- **Approach:** Found the median using a frequency counting array and used virtual index mapping with a three-way partition approach (virtual indexing `(1 + 2 * index) % (n | 1)`) to rearrange elements in-place into alternating wiggle positions without auxiliary sorting calls.
- **Complexity:** $O(n)$ time and $O(1)$ extra space.
- **Edge Case Missed:** Handling clustered duplicate values around the median.

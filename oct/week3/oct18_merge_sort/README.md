# Day 18: Merge Sort & Divide and Conquer

## 1. Merge Two Sorted Lists (LeetCode 21)
- **Approach:** Use a dummy head node and a pointer to iterate through both linked lists simultaneously, attaching the smaller node at each step to the merged list. Finally, append the remaining nodes of the non-empty list.
- **Complexity:** $O(n + m)$ time and $O(1)$ extra space.
- **Edge Case Missed:** One or both lists being completely empty.

## 2. Sort List - Linked List Merge Sort (LeetCode 148)
- **Approach:** Apply top-down merge sort to a linked list. Use the slow and fast pointer technique to split the list into two halves, recursively sort them, and merge the sorted halves using a helper function.
- **Complexity:** $O(n \log n)$ time and $O(\log n)$ space for the recursion stack.
- **Edge Case Missed:** Lists with 0 or 1 node returning immediately without unnecessary recursion.

## 3. Reverse Pairs (LeetCode 493)
- **Approach:** Adapt the merge sort algorithm to count reverse pairs ($i < j$ and $nums[i] > 2 \times nums[j]$). Before merging two sorted halves, count valid pairs using a two-pointer scan across the left and right subarrays.
- **Complexity:** $O(n \log n)$ time and $O(n)$ space.
- **Edge Case Missed:** Arrays with negative numbers and large integer values causing scale checks.

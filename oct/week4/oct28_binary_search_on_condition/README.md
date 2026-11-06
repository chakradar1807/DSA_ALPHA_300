# Day 28: Binary Search on Answer / Allocation Problems

## 1. Koko Eating Bananas (LeetCode 875)
- **Approach:** Applied binary search on the possible eating speeds (`1` to `max(piles)`). Calculated total hours required for each speed using ceiling division arithmetic to find the minimum valid speed.
- **Complexity:** $O(n \log(\max(\text{piles})))$ time and $O(1)$ space.
- **Edge Case Missed:** When the number of available hours equals the total number of piles.

## 2. Capacity To Ship Packages Within D Days (LeetCode 1011)
- **Approach:** Used binary search over the capacity range bounded by the heaviest package and total weight sum. Greedily evaluated whether a given ship capacity can transport all packages within the target days.
- **Complexity:** $O(n \log(\sum \text{weights}))$ time and $O(1)$ space.
- **Edge Case Missed:** Handling cases where the number of allowed days matches the total number of packages.

## 3. Allocate Minimum Pages (GFG)
- **Approach:** Binary searched for the optimal page limit between the maximum single book size and total sum of pages, validating feasibility with a greedy student-allocation counter.
- **Complexity:** $O(n \log(\sum \text{arr}))$ time and $O(1)$ space.
- **Edge Case Missed:** When the number of students exceeds the total number of books (returning `-1`).

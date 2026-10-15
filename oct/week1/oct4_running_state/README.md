# Day 4 - Running state in one pass

## 1. Running Sum of 1d Array (LeetCode 1480)
**Approach:** One pass starting at index 1. Each element adds the element before it, which already holds the running total, so the array is updated in place.
**Time:** O(n)
**Space:** O(1) extra (the input array is modified)
**Edge case missed first time:** (yours)

## 2. Max Consecutive Ones (LeetCode 485)
**Approach:** Keep the current streak and the best streak. A 0 resets the streak, and any other value adds 1. The best is updated after every element, so a streak at the end of the array is counted.
**Time:** O(n)
**Space:** O(1)
**Edge case missed first time:** (yours)

## 3. Best Time to Buy and Sell Stock (LeetCode 121)
**Approach:** Walk the prices once while tracking the lowest price so far. At each day, the best profit if I sell today is the price minus that minimum. Keep the largest profit seen, and it stays 0 if prices only fall.
**Time:** O(n)
**Space:** O(1)
**Edge case missed first time:** (yours)

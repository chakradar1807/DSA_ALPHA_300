# Day 5 - Set membership + missing

## 1. Intersection of Two Arrays (LeetCode 349)
**Approach:** Store every value of nums1 in a dict marked 1. Walk nums2 and change a value's mark to 2 if it is already in the dict. The result is every key marked 2, so duplicates never appear twice.
**Time:** O(n + m)
**Space:** O(n)
**Edge case missed first time:** (yours)

## 2. Missing Number (LeetCode 268)
**Approach:** The numbers 0 to n add up to n * (n + 1) // 2. Add up the array and subtract it from that expected total, and the difference is the missing number.
**Time:** O(n)
**Space:** O(1)
**Edge case missed first time:** (yours)

## 3. Find All Numbers Disappeared in an Array (LeetCode 448)
**Approach:** Put all values in a set. Walk 1 to n, and any number not in the set is missing, so it goes in the result.
**Time:** O(n)
**Space:** O(n)
**Edge case missed first time:** (yours)

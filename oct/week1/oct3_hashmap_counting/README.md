# Day 3 - Hashmap counting

## 1. Majority Element (LeetCode 169)
**Approach:** Boyer-Moore voting. Keep a candidate and a count. If the count is 0, take the current number as the new candidate. Matching numbers add 1 to the count and different numbers subtract 1. The majority element cannot be cancelled out, so it is the candidate left at the end.
**Time:** O(n)
**Space:** O(1)
**Edge case missed first time:** (yours)

## 2. Find Lucky Integer in an Array (LeetCode 1394)
*Substitute for the GFG "Count Frequencies of Array Elements" problem.*
**Approach:** Build a frequency dict by hand with get(num, 0) + 1. Then check each value whose count equals itself and keep the largest. Return -1 if none exists.
**Time:** O(n)
**Space:** O(n)
**Edge case missed first time:** (yours)

## 3. First Unique Character in a String (LeetCode 387)
*Substitute for the GFG "First Non-Repeating Element" problem.*
**Approach:** Pass 1 counts every character in a dict. Pass 2 walks the string in order and returns the first index whose count is 1, or -1 if there is none.
**Time:** O(n)
**Space:** O(1) for lowercase letters (at most 26 keys), O(n) in general
**Edge case missed first time:** (yours)

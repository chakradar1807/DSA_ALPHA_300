# Day 1 - Array and Hashmap Practice

## 1. Two Sum
* **Approach:** I loop through the list once. For every number, I check if its needed counterpart (target minus current number) is already in my dictionary. If it is, I return both indices. If not, I save the current number and keep going.
* **Time:** O(n)
* **Space:** O(n)
* **Edge case handled:** Checking the dictionary *before* saving prevents a number from accidentally pairing with itself (like `[3, 3]` with target `6`).

## 2. Contains Duplicate
* **Approach:** I walk through the array using a set. If I see a number that's already in the set, I return True immediately. If the loop ends without matches, I return False.
* **Time:** O(n)
* **Space:** O(n)
* **Edge case handled:** Arrays with no duplicates or just a single element correctly return False without crashing.

## 3. Single Number
* **Approach:** I use the XOR bitwise operator across all numbers. Duplicate numbers cancel each other out to 0, leaving only the single unique number behind.
* **Time:** O(n)
* **Space:** O(1)
* **Edge case handled:** A single-element array (like `[1]`) skips the cancellation loop and just returns that number as expected.

# Max Sum Subarray

Given an array of integers `arr[]` and an integer `k`, return the maximum sum of any contiguous subarray of size `k`.

A subarray is a contiguous slice of the original array.

## Example

Input:
```
arr[] = [100, 200, 300, 400], k = 2
```
Output:
```
700
```
Explanation: the subarray `[300, 400]` has the maximum sum.

## Constraints

- `1 <= k <= arr.length`
- `arr.length >= k`
- Integers can be negative or positive.

## Solution

The solution uses a sliding window to compute the sum of each contiguous subarray of size `k` in O(n) time.

# Triplets with Smaller Sum

**Difficulty:** Medium  
**Accuracy:** 40.33%  
**Submissions:** 124K+  
**Points:** 4

## Problem Statement

Given an array `arr[]` of distinct integers and a value `sum`, find the count of triplets `(i, j, k)`, having `(i < j < k)` with the sum of `(arr[i] + arr[j] + arr[k])` smaller than the given value `sum`.

## Examples

### Example 1:
```
Input:  sum = 2, arr[] = [-2, 0, 1, 3]
Output: 2
```
**Explanation:** Triplets with sum less than 2 are `(-2, 0, 1)` and `(-2, 0, 3)`.

### Example 2:
```
Input:  sum = 12, arr[] = [5, 1, 3, 4, 7]
Output: 4
```
**Explanation:** Triplets with sum less than 12 are `(1, 3, 4)`, `(5, 1, 3)`, `(1, 3, 7)`, and `(5, 1, 4)`.

## Constraints

- `1 ≤ sum ≤ 10^5`
- `3 ≤ arr.size() ≤ 10^3`
- `-10^3 ≤ arr[i] ≤ 10^3`

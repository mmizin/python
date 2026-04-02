"""
Q2. Find K Pairs with Smallest Sums
Medium
Topics
premium lock icon
Companies
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
"""

import heapq


def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    heap = []


    for n1 in nums1:
        for n2 in nums2:
            item = (n1 + n2, n1, n2)

            if len(heap) < k:
                heapq.heappush_max(heap, item)
            else:
                heapq.heappushpop_max(heap, item)

    return [(n1, n2) for _, n1, n2 in sorted(heap)]



nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print(k_smallest_pairs(nums1, nums2, k))

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2

print(k_smallest_pairs(nums1, nums2, k))


def fastk_smallest_pairs(n1: list[int], n2: list[int], k: int) -> list[list[int]]:
    heap = []
    for i in range(min(k, len(n1))):
        heapq.heappush(heap, (n1[i] + n2[0], i, 0))

    result = []
    while heap and k > len(result):
        _, i, j = heapq.heappop(heap)
        result.append([n1[i], n2[j]])

        if j + 1 < len(n2):
            heapq.heappush(heap, (n1[i] + n2[j+1], i, j + 1))

    return result




nums1 = [1, 2, 3]
nums2 = [4, 5,6]
k = 4

print(fastk_smallest_pairs(nums1, nums2, k))

# Nearest largest element

    arr[] :         [1, 3, 2, 4]
             
    next greater[]: [3, 4, 4, -1]

## Brute force solution

    next_greater = [-1]*N
    for i in range(arr):
        for j in (i+1, range(arr)):
            if arr[j] > arr[i]:
                next_greater[i] = arr[j]


# Using monotonic stack

    class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums2)
        next_greater = [-1]*N
        mn_stack = []
        mn_stack.append(nums2[-1])
        for i in range(N-2, -1, -1):
            if len(mn_stack)>0:
                if nums2[i] > mn_stack[-1]:
                    while((len(mn_stack) > 0) and (nums2[i] > mn_stack[-1])):
                        mn_stack.pop()
            if len(mn_stack)>0:
                next_greater[i] = mn_stack[-1]
            mn_stack.append(nums2[i])
        
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            for j in range(N):
                if nums1[i] == nums2[j]:
                    ans[i] = next_greater[j]
        return ans


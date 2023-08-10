'''
Author : Jyotsna
This function returns the number of pairs for which the sum of the numbers is equal to the given K
Algorithm used - two pointers
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l_i = 0
        r_i = len(nums)-1
        max_ops = 0

        while(l_i < r_i):
            sum_i = nums[l_i] + nums[r_i]
            if sum_i == k:
                l_i += 1
                r_i -= 1
                max_ops += 1

            elif sum_i < k:
                l_i += 1
            else:
                r_i -= 1

        return max_ops
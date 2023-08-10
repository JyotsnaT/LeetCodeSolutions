'''
Author : Jyotsna
This function implements search in a rotated sorted array when elemets are duplicate
'''
# Solution 1: The binary search solution in one pass
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l_i = 0
        r_i = len(nums)-1

        while(l_i <= r_i):
            m_i = l_i + (r_i-l_i)//2
            # print(l_i, m_i, r_i, nums[m_i])
            if nums[m_i] == target:
                return True
            
            # if items m_i == r_i == l_i
            while (l_i < r_i and nums[l_i] == nums[m_i] and nums[m_i] == nums[r_i]):
                l_i += 1
                r_i -= 1
            # print(l_i, r_i)
            if nums[l_i] == target or nums[r_i] == target:
                return True
            # is left subarray sorted
            if nums[l_i] <= nums[m_i] and (nums[l_i] <= target and nums[m_i] >= target):
                # print("cond1")
                r_i = m_i-1
                continue
            elif nums[m_i] <= nums[r_i] and (nums[m_i] <= target and nums[r_i] >= target):
                # print("cond2")
                l_i = m_i + 1
                continue
            l_i += 1
            r_i -= 1
        
        return False
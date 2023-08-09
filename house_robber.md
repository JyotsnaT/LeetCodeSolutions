# [House Robber](https://leetcode.com/problems/house-robber/description/)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police

## Solution 1

Recursive solution without memoization 

    class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        
        currReward = nums[0] + self.rob(nums[2:]) if N>2 else nums[0]
        nextReward = nums[1] + self.rob(nums[3:]) if N>3 else nums[1]
        return max(currReward, nextReward)

Did not get accepted, because of timeout

## Solution 2
Memoization solution

    class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        reward = [0]*N
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums[0], nums[1])
        
        reward[0] = nums[0]
        reward[1] = max(nums[1], reward[0])
        i = 2
        while(i<N): 
            reward[i] = max(nums[i] + reward[i-2], reward[i-1])
            i += 1
        return reward[-1]

 - Runtime - 46ms Beats 54.71%of users with Python3
 - Memory - 16.11mb Beats 94.56%of users with Python3

## Solution 3
Memoization without array

    class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        prevReward = 0
        currReward = 0
        i = 0
        while(i<N): 
            reward_i = max(prevReward+nums[i], currReward)
            prevReward = currReward
            currReward = reward_i
            i += 1
        return currReward

- Runtime 39ms Beats 84.95%of users with Python3
 - Memory 16.38mb Beats 40.48%of users with Python3

'''
Author : Jyotsna
This function returns an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [0]*N

        prefix_prod = 1
        for i in range(N):
            answer[i] = prefix_prod
            prefix_prod *= nums[i]

        postfix_prod = 1
        for i in range(N-1, -1, -1):
            answer[i] *= postfix_prod
            postfix_prod *= nums[i]

        return answer

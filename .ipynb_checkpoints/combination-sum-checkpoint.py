'''
Author : Jyotsna
Here we implement solution to the combination sum I problem from leetcode. Following are the three different DP implementation to the problem.
'''
# Top down DP without memoization
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSum(candidates, target, i):
            # print(candidates, i)
            if i<len(candidates):
                if candidates[i] <= target:
                    combinations1 = combSum(candidates, target-candidates[i], i)
                    combinationsMod = []
                    for comb in combinations1:
                        # print([candidates[i]] + comb)
                        combinationsMod.append([candidates[i]] + comb)
                    if not combinations1 and candidates[i] == target:
                        combinationsMod = [[candidates[i]]]
                    combinations2 = combSum(candidates, target, i+1)
                    return combinationsMod + combinations2
                else:
                    return combSum(candidates, target, i+1)
            else:
                return []
        return combSum(candidates, target, 0)
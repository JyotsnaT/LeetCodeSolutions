class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()

        def min_idx_greatear_than_k(arr, K):
            left_idx = 0
            right_idx = len(arr)-1

            found_greater = False
            least_greatear_idx = -1
            while(left_idx <= right_idx):
                mid = left_idx + (right_idx-left_idx)//2
                if(arr[mid] >= K):
                    found_greater = True
                    least_greater_idx = mid
                    if(mid>0 and arr[mid-1] < K) or mid == 0:
                        break
                    elif(mid>0 and arr[mid-1] >= K):
                        right_idx = mid-1
                else:
                    left_idx = mid+1
            return least_greater_idx if found_greater else len(arr)

        for spell in spells:
            min_potion_strength = math.ceil(success/spell)
            potion_idx = min_idx_greatear_than_k(potions, min_potion_strength)

            potion_count = len(potions) - potion_idx
            pairs.append(potion_count)

        return pairs
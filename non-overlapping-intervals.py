'''
Author : Jyotsna
This function takes in a list of intervals and returns minimum number of intervals one needs to remove to make the rest of the intevals non-overlapping
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], x[0]), reverse=False)

        last_interval = [-6 * 10e4, -6 * 10e4]
        remove_interval = 0
        for interval in intervals:
            if interval[0] >= last_interval[1]:
                last_interval = interval
            else:
                remove_interval += 1
        
        return remove_interval
'''
Author : Jyotsna
This function implements solution for designing a hit counter that returns the number of hits in last 5 minutes
'''

from collections import deque

class HitCounter:
    def __init__(self):
        self.hitCounter = deque()

    def hit(self, timestamp: int) -> None:
        if self.hitCounter:
            while self.hitCounter and timestamp - self.hitCounter[0] >= 300:
                # print(self.hitCounter[0])
                self.hitCounter.popleft()
        self.hitCounter.append(timestamp)
        return 

    def getHits(self, timestamp: int) -> int:
        if self.hitCounter:
            while self.hitCounter and timestamp - self.hitCounter[0] >= 300:
                # print(self.hitCounter[0])
                self.hitCounter.popleft()
        
        return len(self.hitCounter)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
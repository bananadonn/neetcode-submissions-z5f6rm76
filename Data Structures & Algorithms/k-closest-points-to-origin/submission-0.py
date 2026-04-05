import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        index = 0
        for i in points:
            distance = math.sqrt((i[0])**2 + (i[1])**2)
            arr.append([-distance,index])
            index += 1
        
        heapq.heapify(arr)

        while len(arr) > k:
            heapq.heappop(arr)
        kpoints = [points[i] for (_,i) in arr]
        return kpoints
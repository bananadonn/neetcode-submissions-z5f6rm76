class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hmap[num] = 1 + hmap.get(num,0)
        for n, f in hmap.items():
            freq[f].append(n)
        
        res = []
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
            


        
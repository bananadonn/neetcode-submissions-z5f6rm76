class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        def findavg(arr, k):
            sum = 0
            for i in arr:
                sum+= i
            return sum/k

        window = deque()
        total = 0
        for i in range(len(arr)):
            if len(window) == k:
                if findavg(window,k) >= threshold:
                    total += 1
                window.popleft()
                window.append(arr[i])
            else:
                window.append(arr[i])

        if len(window) == k and findavg(window, k) >= threshold:
            total += 1
            
        return total


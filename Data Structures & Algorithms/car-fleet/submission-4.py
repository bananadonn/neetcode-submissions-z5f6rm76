class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for car, position in enumerate(position):
            arr.append((position, car))
        arr = sorted(arr)

        final = {}
        prevmax = 0
        for i in range(len(arr) - 1, -1, -1):
            epochs = (target - arr[i][0]) / speed[arr[i][1]]
            prevmax = max(prevmax, epochs)
            final[prevmax] = 1 + final.get(epochs,0)

        return len(final)
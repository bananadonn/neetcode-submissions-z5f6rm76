class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r = 0,1
        prevsign = ""
        result = 1
        while r < len(arr):
            if arr[r - 1] > arr[r] and prevsign != ">":
                result = max(r - l + 1, result)
                r += 1
                prevsign = ">"
            elif arr[r - 1] < arr[r] and prevsign != "<":
                result = max(result, r - l + 1)
                r += 1
                prevsign = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prevsign = ""

        return result

        
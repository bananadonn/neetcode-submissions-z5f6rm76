class Solution:
    def search(self, nums: List[int], target: int) -> int:
         x = self.recursiveSearch(0,len(nums) -1, nums, target)
         return x
    
    def recursiveSearch(self, L: int, R: int, arr: List[int], target: int) -> int:
        if L > R:
            return -1
        mid = (L + R) // 2
        
        if target < arr[mid]:
            return self.recursiveSearch(L, mid - 1, arr, target)
        elif target > arr[mid]:
            return self.recursiveSearch(mid + 1, R, arr, target)  
        elif target == arr[mid]:
            return mid
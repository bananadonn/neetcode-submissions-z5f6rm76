class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
    
            if nums[l] <= nums[mid]:#left half is sorted
                if target < nums[mid] and target >= nums[l]: #target in left half
                    r = mid - 1
                else: #target in right half
                    l = mid + 1
            
            else:#right half is sorted
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

            
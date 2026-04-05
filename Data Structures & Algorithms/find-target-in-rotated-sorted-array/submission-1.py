class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            #if left half sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]: #target in left half
                    r = mid - 1
                else: #target in right half
                    l = mid + 1 
            #if right half is sorted
            else:
                if nums[r] >= target and target > nums[mid]:#target in right half
                    l = mid + 1
                else: #target in left half
                    r = mid -1
        return -1

                    


            
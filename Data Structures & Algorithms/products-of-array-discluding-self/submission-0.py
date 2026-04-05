class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zeros = set()

        total = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                print(i)
                zeros.add(i)
            else:
                total *= nums[i]
        
        for i in range(len(nums)):
            if i in zeros:
                zeros.remove(i)
                if zeros:
                    output.append(0)
                else:
                    output.append(int(total))
                zeros.add(i)
            else:
                if zeros:
                    output.append(0)
                else:
                    output.append(int(total / nums[i]))
        return output
        
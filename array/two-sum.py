class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            search = target - nums[i]
            # print("works")
            if search in nums[i+1:]:
                # print(nums[i+1:])
                # print(f"{search} is in nums")
                index_2 = nums.index(search, i+1)
                break
        # print(f"my output is:  {[i, index_2]}")
        return [i, index_2]
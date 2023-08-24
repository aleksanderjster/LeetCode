from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in nums[index+1:]:
                return [index, nums.index(compliment)]
            

def main() -> None:
    nums = [3,3] #[2, 7, 11, 15]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)

    

if __name__ == "__main__":
    main()

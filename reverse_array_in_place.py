from typing import List


def reverse(nums: List[int]) -> None:
    start_index = 0
    end_index = len(nums) - 1
    while start_index < end_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1


if __name__ == '__main__':
    nums = [ 4,2,5,6,2 ]
    reverse(nums)
    print(nums)

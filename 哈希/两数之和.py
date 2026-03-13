from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash = dict()
    for i,num in enumerate(nums):
        if target - num in hash:
            return [hash[target-num],i]
        hash[num] = i
    return []
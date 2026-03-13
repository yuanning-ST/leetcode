from typing import List
def subarraySum( nums: List[int], k: int) -> int: #[1],0 [0,1]
    hash = {0:1}
    ans  = 0
    prefix = 0
    for i in range(len(nums)):
        prefix +=nums[i]
        ans+=hash.get(prefix - k, 0)
        hash[prefix]=hash.get(prefix, 0)+1

    return ans

print(subarraySum([1,1,1],2))



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 哈希表记录前缀和出现的次数
        prefix_sum_count = {0: 1}  # 初始前缀和为0，出现1次
        current_sum = 0
        ans = 0
        
        for num in nums:
            current_sum += num  # 计算当前前缀和
            
            # 查找是否存在前缀和等于 current_sum - k
            # 如果存在，说明从那个位置到当前位置的子数组和为k
            ans += prefix_sum_count.get(current_sum - k, 0)
            
            # 更新当前前缀和的出现次数
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return ans
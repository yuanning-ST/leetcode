import heapq  # 需要导入堆模块
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 获取数组长度
        n = len(nums)
        
        # 初始化堆：存储(负数,索引)元组
        # 因为Python的heapq是小根堆，用负数把求最大值问题转为求最小值问题
        q = [(-nums[i], i) for i in range(k)]
        # 将列表转换为堆结构 O(k)
        heapq.heapify(q)
        
        # 第一个窗口的最大值：堆顶的负数取反
        ans = [-q[0][0]]
        
        # 遍历剩余元素，i表示当前窗口的右边界索引
        for i in range(k, n):
            # 1. 将新元素（负数,索引）加入堆中 O(log k)
            heapq.heappush(q, (-nums[i], i))
            
            # 2. 清理过期元素：堆顶索引 <= i-k 说明已滑出窗口
            while q[0][1] <= i - k:
                heapq.heappop(q)  # 弹出过期元素 O(log k)
            
            # 3. 当前堆顶即为窗口最大值（取反后加入结果）
            ans.append(-q[0][0])
        
        return ans

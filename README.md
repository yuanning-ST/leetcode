




## 子串
### 11. 滑动窗口最大值
![alt text](./pic/滑动窗口最大值.png)
```
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
```
### 12. 最小覆盖字串
![alt text](./pic/最小覆盖字串.png)

```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 两个哈希表：ori存储t中每个字符的需求量，cnt存储当前窗口中各字符的存量
        ori = collections.defaultdict(int)  # 需求表
        cnt = collections.defaultdict(int)  # 当前窗口存量表
        
        # 检查当前窗口是否满足需求
        def check() -> bool:
            for c, need_count in ori.items():
                # 如果当前窗口中某个字符的数量小于需求量，则不满足
                if cnt[c] < need_count:
                    return False
            return True
        
        # 初始化需求表：统计t中每个字符的出现次数
        for c in t:
            ori[c] += 1
        
        # 滑动窗口的左右指针
        l = 0
        r = -1  # 初始时窗口为空，r指向-1
        
        # 记录最小窗口的信息
        length = sys.maxsize  # 当前最小窗口长度
        ansL = -1  # 最小窗口的左边界
        ansR = -1  # 最小窗口的右边界（这里其实没用上，但保留原C++风格）
        
        # 扩展右边界，直到遍历完整个s
        while r < len(s) - 1:  # 当r还可以向右移动时
            # 1. 右指针右移，将新字符加入窗口
            r += 1
            # 如果这个字符是t中需要的，则更新存量表
            if s[r] in ori:
                cnt[s[r]] += 1
            
            # 2. 当窗口满足条件时，尝试收缩左边界
            while check() and l <= r:
                # 如果当前窗口比之前记录的最小窗口还小，则更新记录
                if r - l + 1 < length:
                    length = r - l + 1
                    ansL = l  # 记录左边界位置
                
                # 左指针右移前，如果左边要移除的字符是t中需要的，则减少存量
                if s[l] in ori:
                    cnt[s[l]] -= 1
                # 左指针右移，收缩窗口
                l += 1
        
        # 如果没找到符合条件的窗口，返回空字符串；否则返回最小窗口子串
        return "" if ansL == -1 else s[ansL:ansL + length]

```

## 普通数组

### 13. 最大字数组和
![alt text](./pic/最大字数组和.png)

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化当前子数组和为0
        sum = 0
        # 初始化最大子数组和为第一个元素（不能初始化为0，因为可能全是负数）
        max_sum = nums[0]
        
        # 遍历数组中的每个数字
        for num in nums:
            # 如果之前的累加和 >= 0，说明对后续有正向贡献，继续累加
            if sum >= 0:
                sum += num
            # 如果之前的累加和 < 0，说明会拖累后续，舍弃并从当前元素重新开始
            else:
                sum = num
            
            # 更新最大子数组和
            max_sum = max(max_sum, sum)
        
        # 返回最大子数组和
        return max_sum

```

### 14. 合并区间
![alt text](./pic/合并区间.png)

```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. 排序：将所有区间按照起始位置从小到大排序
        # 这样后面只需要顺序处理，保证前面的区间起始值 <= 后面的区间起始值
        intervals.sort(key=lambda x: x[0])

        # 2. 初始化结果列表，用于存放合并后的区间
        merged = []
        
        # 3. 遍历每个区间
        for interval in intervals:
            # 4. 判断条件：如果是第一个区间，或者当前区间与上一个区间不重叠
            # 不重叠的条件是：当前区间的起始值 > 上一个区间的结束值
            if not merged or merged[-1][1] < interval[0]:
                # 5. 不重叠：直接将当前区间加入结果列表
                merged.append(interval)
            else:
                # 6. 重叠：需要合并区间
                # 合并的方式是：保持起始值不变（因为已经排序），结束值取两者的最大值
                # 注意：这里直接修改上一个区间的结束值
                merged[-1][1] = max(merged[-1][1], interval[1])

        # 7. 返回合并后的区间列表
        return merged
```

    sort(): 
    默认升序排列
    numbers = [3, 1, 4, 1, 5]
    numbers.sort()
    print(numbers)  # [1, 1, 3, 4, 5]
    降序排序
    numbers.sort(reverse=True)
    print(numbers)  # [5, 4, 3, 1, 1]

    intervals.sort(key=lambda x: x[0])
    按照每个区间的第一个元素（起始值）进行排序
    分解说明：
    key 参数：指定排序的依据
    lambda x: x[0]：是一个匿名函数，接收一个参数 x（在这里是每个区间），返回 x[0]（区间的起始值）
    排序过程：Python 会根据每个区间返回的起始值大小来排序

### 15. 轮转数组

![alt text](./pic/轮转数组.png)
```
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        旋转数组：将数组中的元素向右移动 k 个位置
        注意：不要返回任何东西，直接修改原数组
        """
        
        # 定义辅助函数：反转数组中指定范围的元素
        def reverse(nums: List[int], start: int, end: int) -> None:
            """
            反转数组 nums 中从 start 到 end 的部分（包含两端）
            例如：reverse([1,2,3,4], 0, 2) → [3,2,1,4]
            """
            # 双指针法，从两端向中间交换元素
            while start < end:
                # 交换 start 和 end 位置的元素
                nums[start], nums[end] = nums[end], nums[start]
                # 左指针右移，右指针左移
                start += 1
                end -= 1
        
        # 1. 处理 k：如果 k 大于数组长度，取余数
        # 例如：数组长度=5，k=7 相当于旋转 7%5=2 次
        k = k % len(nums)
        
        # 2. 核心三步反转法：
        #   这是旋转数组的最优解法，时间复杂度 O(n)，空间复杂度 O(1)
        
        # 第一步：反转整个数组
        # 例如：[1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
        reverse(nums, 0, len(nums) - 1)
        
        # 第二步：反转前 k 个元素
        # 例如：k=3 → 反转前3个 [7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]
        reverse(nums, 0, k - 1)
        
        # 第三步：反转剩下的元素
        # 例如：反转后4个 [5,6,7,4,3,2,1] → [5,6,7,1,2,3,4]
        reverse(nums, k, len(nums) - 1)
        
        # 最终结果：[1,2,3,4,5,6,7] 旋转 k=3 次 → [5,6,7,1,2,3,4]
```
 ### 16. 除自身以外数组的乘积
![alt text](./pic/除自身以外数组的乘积.png)
 ```
 class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        计算除自身以外数组的乘积
        思路：每个位置的答案 = 左边所有数的乘积 * 右边所有数的乘积
        """
        length = len(nums)
        # 初始化结果数组，长度与输入相同
        answer = [0] * length
        
        # === 第一轮遍历：计算每个位置左边所有数的乘积 ===
        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素，所以 answer[0] = 1
        answer[0] = 1
        for i in range(1, length):
            # 左边乘积 = 上一个数 * 上一个数的左边乘积
            # 例如：answer[2] = nums[1] * answer[1]
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # === 第二轮遍历：乘以每个位置右边所有数的乘积 ===
        # R 为右侧所有元素的乘积（动态更新）
        # 刚开始最后一个元素的右边没有元素，所以 R = 1
        R = 1
        # 从右向左遍历
        for i in reversed(range(length)):
            # 对于索引 i：
            # - answer[i] 是左边乘积（第一轮计算好的）
            # - R 是右边乘积（从右向左累加）
            # 最终结果 = 左边乘积 * 右边乘积
            answer[i] = answer[i] * R
            
            # 更新 R：将当前元素乘进去，为下一个左边位置做准备
            # 因为下一个索引 i-1 的右边乘积要包含 nums[i]
            R *= nums[i]
        
        return answer
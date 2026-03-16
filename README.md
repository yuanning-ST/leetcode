




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
```
## 回溯

### 全排列
![alt text](./pic/全排列.png)
```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        全排列（回溯法）
        核心思想：遍历所有数字，每层选一个新数字，用标记数组记录哪些数字已被使用，递归构建排列
        """
        # 初始化结果列表
        self.ans = []
        # 当前正在构建的排列
        self.path = []
        # 标记数组，记录每个位置的数字是否已被使用
        self.used = [False] * len(nums)

        # 定义回溯函数
        def backtrack():
            # 如果当前路径长度等于数组长度，说明找到了一个完整排列
            if len(self.path) == len(nums):
                # 将当前路径的副本加入结果（因为后续会修改）
                self.ans.append(self.path[:])
                return

            # 遍历所有数字
            for i in range(len(nums)):
                # 如果当前数字已被使用，跳过
                if self.used[i]:
                    continue

                # 做选择：将 nums[i] 加入路径，并标记为已使用
                self.used[i] = True
                self.path.append(nums[i])

                # 递归进入下一层
                backtrack()

                # 撤销选择：回溯，恢复状态
                self.path.pop()
                self.used[i] = False

        # 启动回溯
        backtrack()
        return self.ans
```

### 子集
![alt text](./pic/子集.png)
```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        求数组的所有子集（回溯法）
        核心思想：每个元素都有选或不选两种可能，通过回溯枚举所有组合
        """
        # 初始化结果列表和当前路径
        self.ans = []
        self.path = []
        
        def dfs(start: int):
            """
            深度优先搜索
            start: 当前可以选择的起始索引（保证不重复，且顺序递增）
            """
            # 1. 将当前路径加入结果（注意要复制，避免后续修改影响）
            self.ans.append(self.path[:])
            
            # 2. 递归终止条件：如果已经遍历到数组末尾，直接返回
            #    其实这里也可以不写，因为for循环会自动结束
            if start == len(nums):
                return
            
            # 3. 从start开始遍历，依次尝试将每个元素加入路径
            for i in range(start, len(nums)):
                # 做选择：将nums[i]加入路径
                self.path.append(nums[i])
                
                # 递归：下一层从i+1开始，避免重复使用同一个元素
                dfs(i + 1)
                
                # 撤销选择：回溯，恢复状态
                self.path.pop()
        
        # 从索引0开始搜索
        dfs(0)
        return self.ans

```

### 电话号码的字母组合
![alt text](./pic/电话号码的字母组合.png)
```
class Solution:
    def __init__(self):
        # 初始化结果列表和当前路径字符串
        self.ans = []
        self.path = []
        # 数字到字母的映射表
        self.phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        """
        电话号码的字母组合（回溯法）
        核心思想：每个数字对应一组字母，通过回溯枚举所有可能的组合
        """
        # 边界情况：空输入返回空列表
        if not digits:
            return []
        
        # 清空成员变量（防止多次调用时残留）
        self.ans = []
        self.path = []
        
        # 开始回溯
        self.backtrack(digits, 0)
        return self.ans
    
    def backtrack(self, digits: str, index: int):
        """
        回溯函数
        digits: 输入的数字字符串
        index: 当前处理的数字位置
        """
        # 如果已经处理完所有数字，将当前路径加入结果
        if index == len(digits):
            self.ans.append(''.join(self.path))
            return
        
        # 获取当前数字对应的字母串
        letters = self.phone[digits[index]]
        
        # 遍历当前数字的每个字母
        for ch in letters:
            # 做选择：将当前字母加入路径
            self.path.append(ch)
            # 递归处理下一个数字
            self.backtrack(digits, index + 1)
            # 撤销选择：回溯
            self.path.pop()
```

### 组合总和
![alt text](./pic/组合总和.png)
```
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        组合总和（可重复使用同一元素）
        核心思想：回溯法，每次从当前索引开始尝试，避免重复组合
        """
        # 初始化结果列表、当前路径和当前和
        self.ans = []          # 存放所有有效组合
        self.path = []         # 当前正在构建的组合
        self.current_sum = 0   # 当前路径的和
        
        # 开始回溯，从索引0开始
        self.backtrack(candidates, target, 0)
        return self.ans
    
    def backtrack(self, candidates: List[int], target: int, start: int) -> None:
        """
        回溯函数
        candidates: 候选数组
        target: 目标和
        start: 当前可选的起始索引（保证组合递增，避免重复）
        """
        # 剪枝：如果当前和已经超过目标，直接返回
        if self.current_sum > target:
            return
        
        # 找到一个有效组合，加入结果
        if self.current_sum == target:
            # 注意：需要加入当前路径的副本，因为后续会修改
            self.ans.append(self.path[:])
            # 注意：这里没有立即返回，因为后续尝试都会使和变大，但下一层递归会因 >target 而返回
            # 为了效率，也可以在这里加上 return，但原代码没有，我们保留原样
        
        # 从 start 开始遍历，保证每个元素只考虑一次（但可以重复使用，因为下一层仍从当前索引开始）
        for i in range(start, len(candidates)):
            # 做选择：将 candidates[i] 加入路径，并累加和
            self.path.append(candidates[i])
            self.current_sum += candidates[i]
            
            # 递归：因为可以重复使用同一元素，下一层仍从 i 开始
            self.backtrack(candidates, target, i)
            
            # 撤销选择：回溯，恢复状态
            self.path.pop()
            self.current_sum -= candidates[i]

```

### 括号生成
![alt text](./pic/括号生成.png)
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        生成所有有效的括号组合（暴力递归法）
        核心思想：递归生成所有可能的 2^(2n) 种括号序列，然后逐一验证有效性
        """
        # 初始化结果列表和当前路径字符串
        self.ans = []
        self.path = []
        
        def backtrack():
            """回溯生成所有可能的括号序列"""
            # 如果当前路径长度达到 2n，检查是否有效
            if len(self.path) == 2 * n:
                if is_valid(self.path):
                    self.ans.append(''.join(self.path))
                return
            
            # 尝试添加左括号
            self.path.append('(')
            backtrack()
            self.path.pop()
            
            # 尝试添加右括号
            self.path.append(')')
            backtrack()
            self.path.pop()
        
        def is_valid(s: List[str]) -> bool:
            """验证括号序列是否有效"""
            balance = 0
            for ch in s:
                if ch == '(':
                    balance += 1
                else:  # ch == ')'
                    balance -= 1
                if balance < 0:  # 右括号多于左括号，提前失效
                    return False
            return balance == 0  # 最后左右括号数相等
        
        backtrack()
        return self.ans
```

### 单词搜索
![alt text](./pic/单词搜索.png)
```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        判断单词是否存在于二维网格中
        核心思想：回溯 + 剪枝，从每个格子出发深度优先搜索
        """
        # 获取网格的行数和列数
        rows, cols = len(board), len(board[0])
        # 创建访问标记矩阵，初始全为 False
        visited = [[False] * cols for _ in range(rows)]
        
        # 定义四个方向：右、左、下、上
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def backtrack(i: int, j: int, k: int) -> bool:
            """
            从 board[i][j] 开始匹配 word 的第 k 个字符
            返回是否找到一条完整路径
            """
            # 如果当前字符不匹配，直接返回 False
            if board[i][j] != word[k]:
                return False
            
            # 如果已经匹配到最后一个字符，说明找到完整单词
            if k == len(word) - 1:
                return True
            
            # 标记当前格子已访问
            visited[i][j] = True
            
            # 尝试四个方向
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                # 检查新坐标是否在网格范围内
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    # 如果新格子未被访问，则递归探索
                    if not visited[new_i][new_j]:
                        if backtrack(new_i, new_j, k + 1):
                            return True
            
            # 回溯：撤销访问标记
            visited[i][j] = False
            return False
        
        # 遍历每个格子作为起点
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
```

### 分割回文串
![alt text](./pic/分割回文串.png)
```
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        分割回文串
        核心思想：回溯法，从起始位置开始，尝试所有可能的子串，
                如果是回文，则加入当前分割，并递归处理剩余部分
        """
        # 初始化结果列表和当前分割路径
        self.ans = []      # 存放所有有效分割方案
        self.path = []     # 存放当前正在构建的分割
        
        def is_palindrome(sub: str) -> bool:
            """判断子串是否为回文串"""
            left, right = 0, len(sub) - 1
            while left < right:
                if sub[left] != sub[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtrack(start: int):
            """
            回溯函数
            start: 当前开始分割的起始索引
            """
            # 如果已经处理完整个字符串，将当前路径加入结果
            if start == len(s):
                self.ans.append(self.path[:])  # 注意要复制
                return
            
            # 从 start 开始，尝试所有可能的结束位置
            for end in range(start, len(s)):
                # 获取当前子串 [start, end]
                substr = s[start:end+1]
                
                # 如果当前子串不是回文，跳过
                if not is_palindrome(substr):
                    continue
                
                # 做选择：将当前回文子串加入路径
                self.path.append(substr)
                
                # 递归处理剩余部分（从 end+1 开始）
                backtrack(end + 1)
                
                # 撤销选择：回溯
                self.path.pop()
        
        # 从索引0开始回溯
        backtrack(0)
        return self.ans
```

### N皇后
![alt text](./pic/N皇后.png)
```
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        N 皇后问题
        核心思想：回溯法，逐行放置皇后，每行尝试所有列，
                检查当前位置是否与已放置的皇后冲突（同列、对角线）
        """
        # 初始化结果列表和当前路径
        self.ans = []          # 存放所有有效棋盘
        self.path = []         # 当前正在构建的棋盘，每个元素是一个字符串（一行）
        
        def is_safe(col: int) -> bool:
            """
            检查在当前行（即 path 的长度）的 col 列放置皇后是否安全
            需要检查：1. 同一列是否有皇后
                     2. 左上对角线是否有皇后
                     3. 右上对角线是否有皇后
            """
            current_row = len(self.path)  # 当前要放置的行
            for row in range(current_row):
                # 检查同一列
                if self.path[row][col] == 'Q':
                    return False
                # 检查左上对角线：列差 = 行差
                if col - (current_row - row) >= 0 and self.path[row][col - (current_row - row)] == 'Q':
                    return False
                # 检查右上对角线：列差 = 行差
                if col + (current_row - row) < n and self.path[row][col + (current_row - row)] == 'Q':
                    return False
            return True
        
        def backtrack():
            """回溯函数：逐行放置皇后"""
            # 如果已经放满 n 行，说明找到一个有效解
            if len(self.path) == n:
                self.ans.append(self.path[:])  # 注意复制
                return
            
            # 生成当前行的初始字符串，全是 '.'
            row_str = ['.'] * n
            # 尝试当前行的每一列
            for col in range(n):
                if is_safe(col):
                    # 做选择：放置皇后
                    row_str[col] = 'Q'
                    self.path.append(''.join(row_str))
                    
                    # 递归进入下一行
                    backtrack()
                    
                    # 撤销选择：回溯
                    self.path.pop()
                    row_str[col] = '.'  # 恢复当前行的字符
        
        backtrack()
        return self.ans
```
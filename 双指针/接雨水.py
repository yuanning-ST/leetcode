# python 中栈/队列由list实现 取栈顶： -1
from typing import List
def trap(height: List[int]) -> int:
    length = len(height)
    stack = []
    sum = 0
    for i in range(0,length):

        while stack and height[i] > height[stack[-1]]:
            # 弹出底部
            bottom = stack.pop()
            
            # 如果栈为空，说明没有左边界，无法形成凹槽
            if not stack:
                break
                
            # 左边界是栈顶
            left = stack[-1]
            
            # 计算宽度
            width = i - left - 1
            # 计算高度（取左右边界中较小的减去底部高度）
            h = min(height[left], height[i]) - height[bottom]
            
            sum += width * h
        
        # 将当前柱子索引入栈
        stack.append(i)
    return sum

h = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(h))




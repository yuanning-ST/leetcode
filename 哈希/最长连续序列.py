from typing import List
def longestConsecutive(nums: List[int]) -> int:
    hash = set()
    max_len = 0
    
    for num in nums:
        hash.add(num)
    
    for num in hash:
        
        if num-1 in hash:
            continue

        else:
            start = num+1
            while start in hash:
                start+=1
            max_len = max(start-num,max_len)
    
    return max_len
print(longestConsecutive([100,4,200,1,3,2]))


# 先过一遍数组，用哈希记录所有数字
# 再过一遍数组，如果如果num-1在hash，证明他不是开始位置，直到不在hash里，x+1，x+2枚举
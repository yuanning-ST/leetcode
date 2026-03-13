# 
from typing import List
import collections
def findAnagrams(s: str, p: str) -> List[int]:
    # hash_1 = collections.defaultdict(int)
    # hash_2 = collections.defaultdict(int)
    hash_1 = collections.defaultdict(int)
    hash_2 = collections.defaultdict(int)
    ans = []
    for ch in p:
        hash_1[ch]+=1
    
    len_p = len(p)
    for i in range(len_p):
        hash_2[s[i]]+=1
    if hash_1 == hash_2:
        ans.append(0)

    i = 1
    while i+len_p-1<len(s):
        hash_2[s[i+len_p-1]]+=1
        hash_2[s[i-1]]-=1
        if hash_2[s[i - 1]] == 0:
            del hash_2[s[i - 1]]
        if hash_1==hash_2:
            ans.append(i)
        i+=1
    return ans
print(findAnagrams("cbaebabacd","abc"))





# from typing import List

# def findAnagrams(s: str, p: str) -> List[int]:
#     if len(s) < len(p):
#         return []
    
#     hash_1 = {}  # 统计p的字符频率
#     hash_2 = {}  # 统计窗口的字符频率
#     ans = []
    
#     # 统计p中字符频率
#     for ch in p:
#         hash_1[ch] = hash_1.get(ch, 0) + 1
    
#     # 初始化第一个窗口
#     len_p = len(p)
#     for i in range(len_p):
#         hash_2[s[i]] = hash_2.get(s[i], 0) + 1
    
#     # 检查第一个窗口
#     if hash_1 == hash_2:
#         ans.append(0)
    
#     # 滑动窗口
#     for i in range(len_p, len(s)):
#         # 添加新字符
#         hash_2[s[i]] = hash_2.get(s[i], 0) + 1
        
#         # 移除旧字符
#         old_char = s[i - len_p]
#         hash_2[old_char] -= 1
#         # 如果字符计数为0，删除该键
#         if hash_2[old_char] == 0:
#             del hash_2[old_char]
        
#         if hash_1 == hash_2:
#             ans.append(i - len_p + 1)
    
#     return ans

# print(findAnagrams("cbaebabacd", "abc"))  # 输出: [0, 6]
# print(findAnagrams("abab", "ab"))  # 输出: [0, 1, 2]







# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         s_len, p_len = len(s), len(p)
        
#         if s_len < p_len:
#             return []

#         ans = []
#         s_count = [0] * 26
#         p_count = [0] * 26
#         for i in range(p_len):
#             s_count[ord(s[i]) - 97] += 1
#             p_count[ord(p[i]) - 97] += 1

#         if s_count == p_count:
#             ans.append(0)

#         for i in range(s_len - p_len):
#             s_count[ord(s[i]) - 97] -= 1
#             s_count[ord(s[i + p_len]) - 97] += 1
            
#             if s_count == p_count:
#                 ans.append(i + 1)

#         return ans

# 作者：力扣官方题解

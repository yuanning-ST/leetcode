from typing import List
# 哈希可以用set. 或者查询是否有字典键 删除某个键值对可以用del dict 或 dict.pop
#         occ = set()
#         occ.remove(s[i - 1])
#         occ.add(s[rk + 1])
#         xx in occ
# 注意，无法处理重复字符，无法给字符计数

def lengthOfLongestSubstring(s: str) -> int:
    hash = dict()
    ans = 0
    length = len(s)
    j = 0
    for i in range(length):
        if i>0:

            hash.pop(s[i-1])

        while j<length:
            if hash.get(s[j], 0) ==1:
                break
            hash[s[j]] = 1
            j+=1
            ans = max(ans, j-i)
            
    return ans


print(lengthOfLongestSubstring("abcabcbb"))
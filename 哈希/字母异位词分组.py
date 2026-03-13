# C++可以对string排序
# python只能返回有序的列表，故需要把列表再拼成str ''.join(list)
# defaultdict(list) 带默认值的字典
# dict.values/ dict.keys 要类型转换为list
from typing import List
import collections
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hash = collections.defaultdict(list)
    for str in strs:
        key = ''.join(sorted(str))
        hash[key].append(str)
    
    return list(hash.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
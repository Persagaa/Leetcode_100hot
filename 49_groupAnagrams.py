# 给定一个字符串数组，把字母异位词（字母相同、排列不同的词，
# 如 eat 和 tea）归到同一组，返回分组结果。

# AC
class Solution:
    def groupAnagrams(self,str:List[str])->List[List[str]]:
        group=defaultdict(list)
        for s in str:
            key=tuple(sorted(s))
            group[key].append(s)
        return list(group.values())

# ACM
from typing import List
from collections import defaultdict
import sys

class Solution:
    def groupAnagrams(self,str:List[str])->List[List[str]]:
            group=defaultdict(list)
            for s in str:
                key=tuple(sorted(s))
                group[key].append(s)
            return list(group.values())

if "__name__"=="__main__":
     line=sys.stdin.readline().strip()
     inner=line.strip("[]")
     strs=[x.strip().strip('"').strip("'")
           for x in inner.split(",") if x.strip()]
     print(Solution().groupAnagrams(str))
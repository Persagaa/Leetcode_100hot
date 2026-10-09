# 给定未排序的整数数组，找出数字连续的最长序列的长度（不要求元素在原数组中相邻）。
# 要求 O(n) 时间。

#AC
class Solution:
    def LongestConsecutive(self,nums:List[int])->int:
        best=0
        num_set=set(nums)
        for x in num_set:
            if x-1 in num_set:
                continue
            y=x
            while y+1 in num_set:
                y+=y
            best=max(best,y-x+1)
        return best

# ACM
from typing import List
import sys

class Solution:
    def LongestConsecutive(self,nums:List[int])->int:
        best=0
        num_set=set(nums)
        for x in num_set:
            if x-1 in num_set:
                continue
            y=x
            while y+1 in num_set:
                y+=1
            best=max(best,y-x+1)
        return best

if __name__=="__main__":
    line=sys.stdin.readline().strip()
    inner=line.strip("[]")
    nums=list(map(int,inner.split(",")))if inner.strip() else [] 
    print(Solution().LongestConsecutive(nums))
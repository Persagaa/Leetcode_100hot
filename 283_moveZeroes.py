# 给定数组 nums，把所有 0 移到数组末尾，同时保持非零元素的相对顺序。要求原地操作（不复制数组）。

#AC
class Solution:
    def moveZeroes(self,nums:List[int])->None:
        slow=0
        for first_0 in range(len(nums)):
            if nums[first_0]==0:
                slow=first_0
                break
        for fast in range(len(nums)):
            if slow<len(nums) and slow<=fast and nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1

#要保证slow一开始指向第一个0的数值，否则会打乱非零元素顺序
#并且slow一定要严格小于等于fast，否则会打乱0和非零元素顺序

#ACM
from typing import List
import sys

class Solution:
    def moveZeroes(self,nums:List[int])->None:
        slow=0
        for first_0 in range(len(nums)):
            if nums[first_0]==0:
                slow=first_0
                break
        for fast in range(len(nums)):
            if slow<len(nums) and slow<=fast and nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1

if __name__=="__main__":
    line=sys.stdin.readline().strip()
    inner=line.split(',')
    nums=[x for x in inner]
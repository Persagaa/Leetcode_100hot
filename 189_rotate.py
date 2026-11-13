# 题意  给定数组，将元素向右轮转 k 个位置（如 [1,2,3,4,5,6,7] k=3 → [5,6,7,1,2,3,4]）。
# 要求原地且 O(1) 额外空间。

#AC
class Solution:
    def rotate(self,nums:List[int],K:int)->List[int]:
        n=len(nums)
        k%=n
        def rev(l:int,r:int):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
        return nums

#ACM
from typing import List
import sys
class Solution:
    def rotate(self,nums:List[int],K:int)->List[int]:
        n=len(nums)
        k%=n
        def rev(l:int,r:int):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
        return nums

if __name__=="__name__":
    line=sys.stdin.readline().strip()
    inner=line.split(',')
    nums=[int(x) for x in inner]
    k=sys.stdin.readline().strip()
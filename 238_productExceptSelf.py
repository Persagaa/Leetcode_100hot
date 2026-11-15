# 题意  给定数组，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
# 要求不使用除法且 O(n)。

#AC
class Solution:
    def productExceptSelf(self,nums:List[int])->List[int]:
        n=len(nums)
        res=[1]*n
        for i in range(1,n-1):
            res[i]=res[i-1]*nums[i-1]
        right=1
        for i in range(n-1,-1,-1):
            res[i]=right*res[i]
            right=right*nums[i]
        return res

#ACM
from typing import List
import sys

class Solution:
    def productExceptSelf(self,nums:List[int])->List[int]:
        n=len(nums)
        res=[1]*n
        for i in range(1,n-1):
            res[i]=res[i-1]*nums[i-1]
        right=1
        for i in range(n-1,-1,-1):
            res[i]=right*res[i]
            right=right*nums[i]
        return res

if __name__=="__main__":
    line=sys.stdin.readline().strip()
    inner=[int(x) for x in line.split(',')]
    nums=inner
    print(Solution().productExceptSelf(nums))
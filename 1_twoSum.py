# 给定整数数组 nums 和整数目标值 target，请找出数组中和等于 target 的那两个整数，返回它们的数组下标。
# 题目保证恰好存在一组解，同一个元素不能使用两次。

# 思路：遍历nums每一个整数，再用target与之作差，得到的结果在nums中查询是否存在

# AC
# class Solution:
#     def twoSum(self,nums:List[int],target:int)->List[int]:
#         seen={}
#         for i,x in enumerate(nums):
#             if target-x in seen:
#                 return [seen[target-x],i]
#             seen[x]=i

# ACM
from typing import List
import sys 

class Solution:
  def twoSum(self,nums:List[int],target:int)->List[int]:
    seen={}
    for i,x in enumerate(nums):
        if target-x in seen:
            return [seen[target-x],i]
        seen[x]=i
    return []

if __name__=="__main__":
   nums=list(map(int,sys.stdin.readline().strip().strip('[]').split(',')))
   target=int(sys.stdin.readline().strip())
   print(Solution().twoSum(nums,target))
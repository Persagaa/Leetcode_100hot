# 题意  给定未排序整数数组，找出没有出现在数组中的最小正整数。要求 O(n) 时间且 O(1) 空间。
class Solution:
    def firstMissingPositive(self,nums:List[int])->int:
        nums=sorted()
        flag=1
        n=len(nums)
        for i in range(0,n):
            if nums[i]<=0:
                continue
            if nums[i]==flag:
                flag+=1
        return flag


# nums.sort()             # 修法一：原地排，不赋值
# nums = sorted(nums)     # 修法二：换新列表，要赋值

#AC
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 把 nums[i] 换到它应在的位置（值 v 放到下标 v-1）
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


#ACM
#ACM
from typing import List
import sys
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 把 nums[i] 换到它应在的位置（值 v 放到下标 v-1）
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

if __name__=="__main__":
    line=sys.stdin.readline().strip()
    nums=[int(x) for x in line.split(',')]
    print(Solution().firstMissingPositive(nums))


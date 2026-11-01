#239 滑动窗口的最大值
# 题意  给定数组和窗口大小 k，窗口每次右移一格，返回每个窗口位置上的最大值组成的数组。

#AC
class Solution:
    def maxSidingWindows(self,nums:List[int],k:int)->List[int]:
        dp=deque()
        res=[]
        for i,x in enumerate(nums):
            while dp and nums[dp[-1]]<=x:
                dp.pop()
            dp.append(i)
            if dp[0]<=i-k:
                dp.popleft()
            if i>=k-1:
                res.append(nums[dp[0]])
        return res


# 滑动窗口大小为k，即一个窗口为i-k+1~i，所以若取滑动窗口最大值时，i-k+1应该大于等于0

#ACM
import sys 
from typing import List
#typing 是python3.5之后引入的，用于类型提示，可以帮助IDE识别变量类型，避免出错
from collections import deque
#collection里面有很多有用的类，比如deque，Counter，OrderedDict等
#deque是双端队列，可以快速的在两端添加和删除元素
#Counter是计数器，可以快速的统计元素出现的次数
#OrderedDict是有序字典，可以保持元素的顺序
class Solution:
    def maxSidingWindows(self,nums:List[int],k:int)->List[int]:
        dp=deque()
        res=[]
        for i,x in enumerate(nums):
            while dp and nums[dp[-1]]<=x:
                dp.pop()
            dp.append(i)
            if dp[0]<=i-k:
                dp.popleft()
            if i>=k-1:
                res.append(nums[dp[0]])
        return res

if __name__ == "__main__":
    line=sys.stdin.readline().strip()
    inner=line.split(",")
    nums=[int(x) for x in inner]
    n=sys.stdin.readline().strip()
    k=int(n)
    print(Solution().maxSidingWindows(nums,k))
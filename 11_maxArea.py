# 给定 n 条垂直线段的高度，选两条线与 x 轴组成容器，使其能装最多的水（容积 = 两线中较矮者 × 间距），返回最大容积。

#AC
class Solution:
    def maxArea(self,height:List[int])->int:
        l,r,area=0,len(height)-1,0
        while l<r:
            area=max(area,min(height[r],height[l])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area

#ACM
from typing import List
import sys

class Solution:
    def maxArea(self,height:List[int])->int:
        l,r,area=0,len(height)-1,0
        while l<r:
            area=max(area,min(height[r],height[l])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area

if __name__=="__main__":
    line=sys.stdin.readline().strip()
    inner=line.split(",")
    height=[int(x) for x in inner]
    print(Solution().maxArea(height))

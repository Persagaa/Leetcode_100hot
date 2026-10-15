#给定 n 个非负整数表示柱子高度图，计算下雨后能接多少水
#（每个位置上方可蓄的水 = min(左边最高, 右边最高) - 自身高度）


#AC
class Solution:
    def trap(self,heights:List[int])->int:
        l,r=0,len(heights)-1
        rm=lm=area=0
        while l<r:
            rm=max(rm,heights[r])
            lm=max(lm,heights[l])
            if rm>lm:
                area+=lm-heights[l]
                l+=1
            else:
                area+=rm-heights[r]
                r-=1
        return area

#ACM
import sys
from typing import List
class Solution:
    def trap(self,heights:List[int])->int:
        l,r=0,len(heights)-1
        rm=lm=area=0
        while l<r:
            rm=max(rm,heights[r])
            lm=max(lm,heights[l])
            if rm>lm:
                area+=lm-heights[l]
                l+=1
            else:
                area+=rm-heights[r]
                r-=1
        return area

if __name__=="__main__":
    line=sys.stdin.readline().strip()
    inner=line.split(",")
    heights=[int(x) for x in inner]
    area=Solution().trap(heights)
    print(area)
# 给定整数数组，找出所有满足 a+b+c=0 且不重复的三元组。答案中不能包含重复的三元组。

#AC
class Solution:
    def threeSum(self,nums:List[int])->List[List[int]]:
        nums.sort()
        n,res=len(nums),[]
        for i in n-2:
            if nums[i]==nums[i+1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                if nums[l]==nums[r]:
                    break
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    res.append(nums[i],nums[l],nums[r])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1 
        return res    

#ACM
from typing import List
import sys
class Solution:
    def threeSum(self,nums:List[int])->List[List[int]]:
        nums.sort()
        n,res=len(nums),[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1 
        return res    

if __name__=="__main__":
    line=sys.stdin.readline().strpip()
    inner=line.split(",")
    nums=[int(x) for x in inner]
    print(Solution().threeSum(nums))
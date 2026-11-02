from collections import defaultdict
from typing import List
#2026/11/1
#1
# class Solution:
#     def twoSum(self,nums:List[int],target:int)->List[int]:
#         sel={}
#         for i,x in enumerate(nums):
#             if target-x in sel:
#                 return [sel[target-x],i]
#             sel[x]=i
#2
# class Solution:
#     def sameString(self,strs:List[str])->List[List[int]]:
#         groupby=defaultdict(list)
#         for x in strs:
#             key=tuple(sorted(x))
#             groupby[key].append(x)
#         return [groupby.values()]
#3
# class Solution:
#     def maxLength(self,nums:List[int])->int:
#         num_set=set(nums)
#         best=0
#         for x in nums:
#             if x-1 in nums:
#                 continue
#             y=x
#             while y+1 in nums:
#                 y=y+1
#             best=max(best,y-x+1)
#         return best
#4***
# class Solution:
#     def move0(self,nums:List[int])->List:
#         slow=fast=0
#         for fast in range(len(nums)):
#             if nums[fast]!=0:
#                 nums[slow],nums[fast]=nums[fast],nums[slow]
#                 slow+=1
#5***#既要考虑更高的，也要考虑更远的
# class Solution:
#     def maxWater(self,nums:list[int])->int:
#         l,r=0,len(nums)-1
#         area=0
#         while l<r:
#             area=max(area,min(nums[l],nums[r])*(r-l))
#             if nums[l]<nums[r]:
#                 l+=1
#             else:
#                 r-=1
#         return area
#6***********************
class Solution:
    def threeSum(self,nums:List[int])->List[List[int]]:
        nums.sort()
        n,res=len(nums),[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                s=nums[l]+nums[r]+nums[i]
                if l<r and s>0:
                    r-=1
                elif l<r and s<0:
                    l+=1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1; r -= 1
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
        return res
#7
class Solution:
    def rainSum(self,nums:List[int])->int:
        n,sum=len(nums),0
        for x in range(1,n-1):
            l,r=0,n-1
            lmax=nums[l]
            rmax=nums[r]
            while l<x:
                lmax=max(nums[l],lmax)
                l+=1
            while r>x:
                rmax=max(nums[r],rmax)
                r-=1
            height=min(lmax,rmax)
            sum+=max(0,height-nums[x])
        return sum
#8************重复字符不一定放在一起
class Solution:
    def norepeat(self,s:str)->int:
        win=set()
        l=0
        length=0
        n=len(s)
        for x in range(n):
            if s[x] in win:
                while s[x] in win:
                    win.remove(s[l])
                    l+=1
            win.add(s[x])
            length=max(length,x-l+1)
        return length



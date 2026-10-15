#给定整数数组和一个整数 k，统计该数组中和恰好等于 k 的连续子数组的个数。

#AC
class Solution:
    def subarrySum(self,nums:list[int],k:int)->int:
        cnt=DefaultDict(int)
        cnt[0]=1
        pre=ans=0
        for x in nums:
            pre+=x
            ans+=cnt[pre-k]
            cnt[pre]+=1
        return ans 
            
#ACM
import sys
from typing import DefaultDict
class Solution:
    def subarrySum(self,nums:list[int],k:int)->int:
        cnt=DefaultDict(int)
        cnt[0]=1
        pre=ans=0
        for x in nums:
            pre+=x
            ans+=cnt[pre-k]
            cnt[pre]+=1
        return ans 
    
if __name__=="__main__":
    line=sys.stdin.readline().strip()
    inner=line.split(",")
    nums=[int(x) for x in inner]
    n=sys.stdin.readline().strip()
    k=int(n)
    print(Solution().subarrySum(nums,k))



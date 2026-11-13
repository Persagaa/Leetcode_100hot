# 给定一个字符串数组，把字母异位词（字母相同、排列不同的词，
# 如 eat 和 tea）归到同一组，返回分组结果。

# 复杂度：时间O(n*k*logk)(k为字符串最大长度)，空间O(n*k)
# AC
class Solution:
    def groupAnagrams(self,str:List[str])->List[List[str]]:
        group=defaultdict(list)
        for s in str:
            key=tuple(sorted(s))
            group[key].append(s)
        return list(group.values())

# ACM
from typing import List
import sys
class Solution:
    def rotate(self,nums:List[int],k:int)->List[int]:
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

if __name__=="__main__":
    line=sys.stdin.readline().strip()
    inner=line.split(',')
    nums=[int(x) for x in inner]
    k=sys.stdin.readline().strip()
    k=int(k)
    print(Solution().rotate(nums,k))


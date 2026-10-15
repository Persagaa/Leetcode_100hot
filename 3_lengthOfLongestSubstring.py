#给定字符串 s，找出不含重复字符的最长子串的长度。

import enumerate

#AC
class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        win=set()
        l=ans=0
        for r,c in enumerate(s):
            while c in win:
                win.remove(s[l])
                l+=1
            win.add(c)
            ans=max(ans,r-l+1)
        return ans

#ACM
import sys

class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        win=set()
        l=ans=0
        for r,c in enumerate(s):
            while c in win:
                win.remove(s[l])
                l+=1
            win.add(c)
            ans=max(ans,r-l+1)
        return ans

if __name__=="__main__":
    s=sys.stdin.readline().strip()
    print(Solution().lengthOfLongestSubstring(s))


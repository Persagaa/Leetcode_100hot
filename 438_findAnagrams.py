#给定字符串 s 和模式串 p，找出 s 中所有 p 的异位词（字母重排）子串的起始下标。

#AC
class Solution:
    def findAnagrams(self,s:str,p:str)->int:
        n=len(p)
        m=len(s)
        #如果字符串比模式串短，说明没有
        if m<n:
            return []
        need=Counter(p)
        win=Counter(s[:n])
        res=[0] if need==win else []
        for x in range(n,m):
            win[s[x]]+=1
            win[s[x-n]]-=1
            if win[s[x-n]]==0:
                del win[s[x-n]]
            if win==need:
                res.append(x-n+1)
        return res

#ACM
import sys
from collections import Counter

class Solution:
    def findAnagrams(self,s:str,p:str)->int:
        n=len(p)
        m=len(s)
        #如果字符串比模式串短，说明没有
        if m<n:
            return []
        need=Counter(p)
        win=Counter(s[:n])
        res=[0] if need==win else []
        for x in range(n,m):
            win[s[x]]+=1
            win[s[x-n]]-=1
            if win[s[x-n]]==0:
                del win[s[x-n]]
            if win==need:
                res.append(x-n+1)
        return res
if __name__=="__main__":
    s=sys.stdin.readline().strip()
    p=sys.stdin.readline().strip()
    print(Solution().findAnagrams(s,p))

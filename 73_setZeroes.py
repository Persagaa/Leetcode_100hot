# 给定 m×n 矩阵，若某元素为 0，则将其所在行与列全部置 0。
# 要求原地算法（最好 O(1) 额外空间）。

#AC
class Solution:
    def setZeroes(self,matrix:List[List[int]])->None:
        m,n=len(matrix),len(matrix[0])
        first_row=any(matrix[i][0] for i in range(m))
        first_col=any(matrix[0][j] for j in range(n))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,m):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if first_row==True:
            for i in range(0,n):
                matrix[0][i]=0
        if first_col==True:
            for j in range(0,m):
                matrix[j][0]=0

#ACM
from typing import List
import sys

class Solution:
    def setZeroes(self,matrix:List[List[int]])->None:
        m,n=len(matrix),len(matrix[0])
        first_row=any(matrix[i][0]==0 for i in range(m))
        first_col=any(matrix[0][j]==0 for j in range(n))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if first_row==True:
            for i in range(0,n):
                matrix[0][i]=0
        if first_col==True:
            for j in range(0,m):
                matrix[j][0]=0

def build_matrix(tokens):
    m,n=int(tokens[0]),int(tokens[1]) #第一行：行数，列数
    vals=[int(x) for x in tokens[2:2+m*n]]  #后面 m*n个数
    return [vals[i*n:(i+1)*n] for i in range(m)]
    # 为什么？因为每行占 n 个位置，排在第 i 行前面已经躺了 i 整行​ = i × n 个数
    # 终点自然是下一行的起点 (i+1)*n

if __name__=="__main__":
    data=sys.stdin.read().replace(',',' ').split()
    if not data:
        sys.exit(0)
    matrix=build_matrix(data)
    Solution().setZeroes(matrix)
    for row in matrix:
        print(' '.join(map(str,row)))
    # 手动敲 → 敲完按 Ctrl+Z 再回车（Windows）表示 EOF；
    # 只敲一行回车它会一直挂着，这跟前几轮 readline() 那种"空跑就 int('') 炸"是不同的挂法
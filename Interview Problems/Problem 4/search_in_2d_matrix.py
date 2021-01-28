# -*- coding: utf-8 -*-
"""Search in 2D Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/149xOMMI4ZuCiuhD2qu2-iRT58hQZW0D1
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      row = len(matrix)
      column = len(matrix[0])
        
      if row == 0:
        return False
        row_start = 0
        row_end = row - 1
        
        # Binary Search Row Wise
        while(row_start < row_end):
          row_mid = row_start + (row_end - row_start)//2
          if matrix[row_mid][column - 1] < target:
            row_start = row_mid + 1
          elif matrix[row_mid][0] > target:
            row_end = row_mid - 1
            else:
              row_start = row_mid
              break
                
        col_start = 0
        col_end = column - 1
        # Binary Search Column Wise
        while(col_start <= col_end):
          col_mid = col_start + (col_end - col_start)//2
          if matrix[row_start][col_mid] < target :
            col_start = col_mid + 1
            elif matrix[row_start][col_mid] > target:
              col_end = col_mid - 1
              else:
                return True
        return False
# -*- coding: utf-8 -*-
"""18310.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QOCmb7kojIjNXfE80WP19cwLGTsh4hUw
"""

n= int(input())
rocation = list(map(int, input().split()))
print(rocation)

stack = [[0] for _ in range(n)]
p=100001
min_sum=999999999

print(stack)

for i in range(n):
  sum=0
  sum += stack[i][0]
  p_val = rocation[i]
  for j in range(i+1,n):
    value = abs(p_val - rocation[j])
    sum += value
    stack[j][0] += value 
    print("sum:",sum)
    print(stack)
  if sum == min_sum and p > p_val :
    p = p_val
  elif sum < min_sum:
    min_sum = sum
    p = p_val
    print(min_sum)
    print(p)
  print("--------------")

print(p)


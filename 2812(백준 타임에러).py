# -*- coding: utf-8 -*-
"""2812.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xCrPVHzpGkVjNKHSgIkNRrc74WHgqqD0
"""

#시도1
n, k=map(int, input().split())
num=list(map(int, input()))
max_num=[]

def findmax(i,j,arr):
  maxval=arr[i]
  max_index=i
  for a in range(i,j+1):
    if (maxval<arr[a]):
      maxval=arr[a]
      max_index=a
  return maxval, max_index

i=0
j=k
for ii in range(n-k):
  p, idx=findmax(i,j,num)
  max_num.append(p)
  i=idx+1
  j+=1
  print(max_num[ii],end='')

#시도2
n, k=map(int, input().split())
num=list(map(str, input()))
is_num=[0,1,2,3,4,5,6,7,8,9]

for i in is_num:
  if (k==0):
    break
  cnt=num.count(str(i))
  for _ in range(cnt):
    print("aa")
    if (k==0):
      break
    num.remove(str(i))
    k-=1


print(int("".join(num)))


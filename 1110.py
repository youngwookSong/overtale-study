# -*- coding: utf-8 -*-
"""1110.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lh98TMt5XnyG8LIDVCNJ1tMJotBMzOCn
"""

a=list(map(int, list(str(input()))))
if(len(a)==1):
  a.insert(0,0)
n=a[0]*10 + a[1]
cnt=1

while(1):
  p=[]
  if(len(a)==1):
    a.insert(0,0)
  p.append(a[1]) 
  p.append(sum(a)%10)
  if((p[0]*10 + p[1]) == n):
    break;
  a[0]=p[0]
  a[1]=p[1]
  cnt=cnt+1

print(cnt)

